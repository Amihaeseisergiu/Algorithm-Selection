package process.metric;

import java.lang.management.ManagementFactory;
import java.time.Duration;
import java.time.Instant;
import java.util.concurrent.TimeUnit;

import com.sun.management.OperatingSystemMXBean;
import org.json.JSONObject;
import process.pubsub.AlgorithmsDataPublisher;
import process.pubsub.Publisher;
import process.pubsub.UserPublisher;

public class Profiler {
    private final String socketId;
    private final String fileId;
    private final String algorithmName;
    private final String algorithmType;

    private final Runtime runtime;
    private final OperatingSystemMXBean os;

    volatile boolean initialized = false;
    volatile boolean initializedMemorySet = false;
    volatile boolean stopped = false;
    volatile long emittedDataPoints = 1;
    volatile double totalMemory = 0;
    volatile double totalCpu = 0;
    volatile double lastRecordedTime = 0;
    volatile double initializationMemory = 0;
    Instant startTime;

    private final Publisher userPublisher;
    private final Publisher algorithmPublisher;

    public Profiler(String socketId, String fileId, String algorithmName, String algorithmType) {
        this.socketId = socketId;
        this.fileId = fileId;
        this.algorithmName = algorithmName;
        this.algorithmType = algorithmType;

        this.runtime = Runtime.getRuntime();
        this.os = ManagementFactory.getPlatformMXBean(com.sun.management.OperatingSystemMXBean.class);

        this.userPublisher = new UserPublisher(socketId, algorithmName);
        this.algorithmPublisher = new AlgorithmsDataPublisher(fileId, algorithmName, algorithmType);
    }

    private double getMemory() {
        return (double) (runtime.totalMemory() - runtime.freeMemory()) / (1024L * 1024L);
    }

    private double getCpu() {
        return os.getCpuLoad() * 100;
    }

    private double getTime() {
        Instant currentTime = Instant.now();

        return (double) Duration.between(startTime, currentTime).toMillis() / 1000;
    }

    private synchronized void emit() {
        double currentMemory = getMemory() - initializationMemory;
        double currentCpu = getCpu();
        double currentTime = getTime();

        if (initialized && currentMemory >= 0) {
            totalMemory += currentMemory;
            totalCpu += currentCpu;
            emittedDataPoints += 1;
        }

        if (initialized && (!initializedMemorySet || currentMemory < 0)) {
            initializationMemory = getMemory();
            initializedMemorySet = true;

            if (currentMemory < 0) {
                currentMemory = initializationMemory;
            } else {
                currentMemory = 0;
            }
        }

        lastRecordedTime = currentTime;

        JSONObject userData = new JSONObject()
                .put("event_name", "metric_emit")
                .put("payload", new JSONObject()
                        .put("algorithm_name", algorithmName)
                        .put("metrics", new JSONObject()
                                .put("memory", currentMemory)
                                .put("cpu", currentCpu)
                        )
                        .put("time", currentTime)
                );

        userPublisher.send(userData);
    }

    private void postEmit() {
        JSONObject userData = new JSONObject()
                .put("event_name", "metric_end")
                .put("payload", new JSONObject()
                        .put("algorithm_name", algorithmName)
                        .put("time", lastRecordedTime)
                );

        userPublisher.send(userData);

        JSONObject aggregatorData = new JSONObject()
                .put("avg_memory", totalMemory / emittedDataPoints)
                .put("avg_cpu", totalCpu / emittedDataPoints)
                .put("total_time", lastRecordedTime);

        algorithmPublisher.send(aggregatorData);
    }

    private void monitor() {
        startTime = Instant.now();

        while (!stopped) {
            try {
                TimeUnit.MILLISECONDS.sleep(100);
                emit();
            } catch (InterruptedException e) {
                stopped = true;
                e.printStackTrace();
            }
        }

        postEmit();
    }

    public void markInitialization() {
        System.gc();
        initialized = true;
    }

    public Thread start() {
        Thread thread = new Thread(this::monitor);
        thread.start();

        return thread;
    }

    public void stop() {
        stopped = true;
    }
}

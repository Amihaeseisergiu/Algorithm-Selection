package process;

import org.json.JSONObject;
import process.algorithm.Algorithm;
import process.algorithm.Algorithms;
import process.instance.Instance;
import process.instance.InstanceRepository;
import process.pubsub.Publisher;
import process.pubsub.AlgorithmsDataPublisher;
import process.pubsub.UserPublisher;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        String instancePath = args[0];
        String algorithmName = args[1];
        String algorithmType = args[2];
        String fileId = args[3];
        String socketId = args[4];
        double start_time = Double.parseDouble(args[5]);

        List<Publisher> algorithmPublishers = List.of(
                new AlgorithmsDataPublisher(fileId, algorithmName, algorithmType)
        );

        Instance instance = InstanceRepository.getInstance(instancePath);
        Algorithm algorithm = Algorithms.getMapping(instance, algorithmPublishers).get(algorithmName);

        Publisher userPublisher = new UserPublisher(socketId, algorithmName);
        Publisher algorithmsDataPublisher = new AlgorithmsDataPublisher(fileId, algorithmName, algorithmType);

        double initializationTime = System.currentTimeMillis() / 1000.0 - start_time;
        userPublisher.send(
                new JSONObject()
                        .put("event_name", "init_time")
                        .put("payload", new JSONObject()
                                .put("init_time_end", initializationTime)
                        )
        );
        algorithmsDataPublisher.send(
                new JSONObject()
                        .put("initialization_time", initializationTime)
        );

        algorithm.run();
    }
}
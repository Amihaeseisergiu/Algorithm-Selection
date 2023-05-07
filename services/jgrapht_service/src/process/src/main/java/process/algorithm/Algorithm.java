package process.algorithm;

import com.jsoniter.any.Any;
import org.jgrapht.Graph;
import org.jgrapht.graph.DefaultEdge;
import org.json.JSONObject;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

public abstract class Algorithm {
    protected Graph<Integer, DefaultEdge> graph;
    protected Any parameters;
    protected List<Publisher> publishers;
    protected volatile double bestHeuristicScore = Double.MAX_VALUE;
    protected volatile double bestResult = Double.MAX_VALUE;

    protected Algorithm(Instance instance, List<Publisher> publishers) {
        this.graph = instance.graph();
        this.parameters = instance.parameters();
        this.publishers = publishers;
    }

    protected abstract void algorithm();

    public void run() {
        ExecutorService executor = Executors.newSingleThreadExecutor();
        Future<?> future = executor.submit(this::algorithm);

        try {
            future.get(Integer.parseInt(System.getenv("ALGORITHM_TIMEOUT")), TimeUnit.SECONDS);
        } catch (TimeoutException | InterruptedException | ExecutionException e) {
            future.cancel(true);
        }

        executor.shutdownNow();
        publishResult(bestResult, bestHeuristicScore);
    }

    private void publishResult(double result, double heuristicScore) {
        for(Publisher publisher : publishers) {
            publisher.send(new JSONObject()
                    .put("result", result)
                    .put("heuristic_score", heuristicScore)
            );
        }
    }
}

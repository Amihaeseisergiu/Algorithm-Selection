package process.algorithm;

import com.jsoniter.any.Any;
import org.jgrapht.Graph;
import org.jgrapht.graph.DefaultEdge;
import org.json.JSONObject;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.List;

public abstract class Algorithm {
    protected Graph<String, DefaultEdge> graph;
    protected Any parameters;
    protected List<Publisher> publishers;

    protected Algorithm(Instance instance, List<Publisher> publishers) {
        this.graph = instance.graph();
        this.parameters = instance.parameters();
        this.publishers = publishers;
    }

    protected abstract double algorithm();

    public void run() {
        double result = algorithm();
        publishResult(result);
    }

    private void publishResult(double result) {
        for(Publisher publisher : publishers) {
            publisher.send(new JSONObject().put("result", result));
        }
    }
}

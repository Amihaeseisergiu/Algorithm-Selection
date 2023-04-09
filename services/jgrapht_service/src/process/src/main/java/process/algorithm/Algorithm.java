package process.algorithm;

import com.jsoniter.any.Any;
import org.jgrapht.Graph;
import org.jgrapht.graph.DefaultEdge;
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

    protected abstract String algorithm();

    public void run() {
        String result = algorithm();
        publishResult(result);
    }

    private void publishResult(String result) {
        for(Publisher publisher : publishers) {
            publisher.send(result);
        }
    }
}

package process.algorithm.shortestpath;

import org.jgrapht.GraphPath;
import org.jgrapht.alg.shortestpath.BellmanFordShortestPath;
import org.jgrapht.graph.DefaultEdge;
import process.algorithm.Algorithm;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.List;

public class BellmanFord extends Algorithm {
    String source;
    String target;

    public BellmanFord(Instance instance, List<Publisher> publishers) {
        super(instance, publishers);
        this.source = parameters.get("source").toString();
        this.target = parameters.get("target").toString();
    }

    public String algorithm() {
        BellmanFordShortestPath<String, DefaultEdge> bellmanFordShortestPath = new BellmanFordShortestPath<>(this.graph);
        GraphPath<String, DefaultEdge> path = bellmanFordShortestPath.getPath(this.source, this.target);

        return String.valueOf(path.getLength());
    }
}

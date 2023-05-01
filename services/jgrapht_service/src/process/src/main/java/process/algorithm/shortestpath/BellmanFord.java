package process.algorithm.shortestpath;

import org.jgrapht.GraphPath;
import org.jgrapht.alg.shortestpath.BellmanFordShortestPath;
import org.jgrapht.graph.DefaultEdge;
import process.algorithm.Algorithm;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.List;

public class BellmanFord extends Algorithm {
    int source;
    int target;

    public BellmanFord(Instance instance, List<Publisher> publishers) {
        super(instance, publishers);
        this.source = parameters.get("source").toInt();
        this.target = parameters.get("target").toInt();
    }

    public double algorithm() {
        BellmanFordShortestPath<Integer, DefaultEdge> bellmanFordShortestPath = new BellmanFordShortestPath<>(this.graph);
        GraphPath<Integer, DefaultEdge> path = bellmanFordShortestPath.getPath(this.source, this.target);

        return path.getLength();
    }
}

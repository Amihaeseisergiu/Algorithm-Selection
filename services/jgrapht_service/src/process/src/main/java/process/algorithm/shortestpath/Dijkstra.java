package process.algorithm.shortestpath;

import org.jgrapht.GraphPath;
import org.jgrapht.alg.shortestpath.DijkstraShortestPath;
import org.jgrapht.graph.DefaultEdge;
import process.algorithm.Algorithm;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.List;

public class Dijkstra extends Algorithm {
    String source;
    String target;

    public Dijkstra(Instance instance, List<Publisher> publishers) {
        super(instance, publishers);
        this.source = parameters.get("source").toString();
        this.target = parameters.get("target").toString();
    }

    public String algorithm() {
        DijkstraShortestPath<String, DefaultEdge> dijkstraShortestPath = new DijkstraShortestPath<>(this.graph);
        GraphPath<String, DefaultEdge> path = dijkstraShortestPath.getPath(this.source, this.target);

        return String.valueOf(path.getLength());
    }
}

package process.algorithm.shortestpath;

import org.jgrapht.GraphPath;
import org.jgrapht.alg.shortestpath.DijkstraShortestPath;
import org.jgrapht.graph.DefaultEdge;
import process.algorithm.Algorithm;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.List;

public class Dijkstra extends Algorithm {
    int source;
    int target;

    public Dijkstra(Instance instance, List<Publisher> publishers) {
        super(instance, publishers);
        this.source = parameters.get("source").toInt();
        this.target = parameters.get("target").toInt();
    }

    public void algorithm() {
        DijkstraShortestPath<Integer, DefaultEdge> dijkstraShortestPath = new DijkstraShortestPath<>(this.graph);
        GraphPath<Integer, DefaultEdge> path = dijkstraShortestPath.getPath(this.source, this.target);

        bestResult = path.getLength();
    }
}

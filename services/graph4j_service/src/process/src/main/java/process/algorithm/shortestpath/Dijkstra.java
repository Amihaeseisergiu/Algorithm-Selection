package process.algorithm.shortestpath;

import org.graph4j.alg.sp.DijkstraShortestPathDefault;
import org.graph4j.util.Path;
import process.algorithm.Algorithm;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.List;

public class Dijkstra extends Algorithm {
    Integer source;
    Integer target;

    public Dijkstra(Instance instance, List<Publisher> publishers) {
        super(instance, publishers);
        this.source = parameters.get("source").toInt();
        this.target = parameters.get("target").toInt();
    }

    public String algorithm() {
        DijkstraShortestPathDefault dijkstraShortestPath = new DijkstraShortestPathDefault(this.graph, this.source);
        Path path = dijkstraShortestPath.findPath(this.target);

        return String.valueOf(path.length());
    }
}

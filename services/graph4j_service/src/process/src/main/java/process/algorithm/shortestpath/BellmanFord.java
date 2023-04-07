package process.algorithm.shortestpath;

import org.graph4j.alg.sp.BellmanFordShortestPath;
import org.graph4j.util.Path;
import process.algorithm.Algorithm;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.List;

public class BellmanFord extends Algorithm {
    Integer source;
    Integer target;

    public BellmanFord(Instance instance, List<Publisher> publishers) {
        super(instance, publishers);
        this.source = parameters.get("source").toInt();
        this.target = parameters.get("target").toInt();
    }

    public String algorithm() {
        BellmanFordShortestPath bellmanFordShortestPath = new BellmanFordShortestPath(this.graph, this.source);
        Path path = bellmanFordShortestPath.findPath(this.target);

        return String.valueOf(path.length());
    }
}

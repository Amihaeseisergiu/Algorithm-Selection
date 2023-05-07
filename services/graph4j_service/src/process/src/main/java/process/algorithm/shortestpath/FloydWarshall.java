package process.algorithm.shortestpath;

import org.graph4j.alg.sp.FloydWarshallShortestPath;
import org.graph4j.util.Path;
import process.algorithm.Algorithm;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.List;

public class FloydWarshall extends Algorithm {
    Integer source;
    Integer target;

    public FloydWarshall(Instance instance, List<Publisher> publishers) {
        super(instance, publishers);
        this.source = parameters.get("source").toInt();
        this.target = parameters.get("target").toInt();
    }

    public void algorithm() {
        FloydWarshallShortestPath bellmanFordShortestPath = new FloydWarshallShortestPath(this.graph);
        Path path = bellmanFordShortestPath.findPath(this.source, this.target);

        bestResult = path.length();
    }
}

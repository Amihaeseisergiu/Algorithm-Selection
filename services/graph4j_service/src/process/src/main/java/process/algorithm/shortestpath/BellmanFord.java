package process.algorithm.shortestpath;

import org.graph4j.Graph;
import org.graph4j.alg.sp.BellmanFordShortestPath;
import org.graph4j.util.Path;
import process.algorithm.Algorithm;
import process.instance.Instance;

public class BellmanFord extends Algorithm {
    Integer source;
    Integer target;
    Graph graph;

    public BellmanFord(Instance instance) {
        super(instance);
        this.graph = instance.graph();
        this.source = instance.parameters().get("source").toInt();
        this.target = instance.parameters().get("target").toInt();
    }

    public void run() {
        BellmanFordShortestPath bellmanFordShortestPath = new BellmanFordShortestPath(this.graph, this.source);
        Path path = bellmanFordShortestPath.findPath(this.target);
        System.out.println("BellmanFord path length: " + path.length());
    }
}

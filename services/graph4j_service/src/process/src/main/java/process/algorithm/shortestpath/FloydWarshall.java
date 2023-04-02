package process.algorithm.shortestpath;

import org.graph4j.Graph;
import org.graph4j.alg.sp.FloydWarshallShortestPath;
import org.graph4j.util.Path;
import process.algorithm.Algorithm;
import process.instance.Instance;

public class FloydWarshall extends Algorithm {
    Integer source;
    Integer target;
    Graph graph;

    public FloydWarshall(Instance instance) {
        super(instance);
        this.graph = instance.graph();
        this.source = instance.parameters().get("source").toInt();
        this.target = instance.parameters().get("target").toInt();
    }

    public void run() {
        FloydWarshallShortestPath bellmanFordShortestPath = new FloydWarshallShortestPath(this.graph);
        Path path = bellmanFordShortestPath.findPath(this.source, this.target);
        System.out.println("FloydWarshall path length: " + path.length());
    }
}

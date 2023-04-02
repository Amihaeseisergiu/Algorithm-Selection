package process.algorithm.shortestpath;

import org.graph4j.Graph;
import org.graph4j.alg.sp.DijkstraShortestPathDefault;
import org.graph4j.util.Path;
import process.algorithm.Algorithm;
import process.instance.Instance;

public class Dijkstra extends Algorithm {
    Integer source;
    Integer target;
    Graph graph;

    public Dijkstra(Instance instance) {
        super(instance);
        this.graph = instance.graph();
        this.source = instance.parameters().get("source").toInt();
        this.target = instance.parameters().get("target").toInt();
    }

    public void run() {
        DijkstraShortestPathDefault dijkstraShortestPath = new DijkstraShortestPathDefault(this.graph, this.source);
        Path path = dijkstraShortestPath.findPath(this.target);
        System.out.println("Dijkstra path length: " + path.length());
    }
}

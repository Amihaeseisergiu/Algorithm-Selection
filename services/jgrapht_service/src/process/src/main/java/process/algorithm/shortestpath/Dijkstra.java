package process.algorithm.shortestpath;

import org.jgrapht.Graph;
import org.jgrapht.GraphPath;
import org.jgrapht.alg.shortestpath.DijkstraShortestPath;
import org.jgrapht.graph.DefaultEdge;
import process.algorithm.Algorithm;
import process.instance.Instance;

public class Dijkstra extends Algorithm {
    String source;
    String target;
    Graph<String, DefaultEdge> graph;

    public Dijkstra(Instance instance) {
        super(instance);
        this.graph = instance.graph();
        this.source = instance.parameters().get("source").toString();
        this.target = instance.parameters().get("target").toString();
    }

    public void run() {
        DijkstraShortestPath<String, DefaultEdge> dijkstraShortestPath = new DijkstraShortestPath<>(this.graph);
        GraphPath<String, DefaultEdge> path = dijkstraShortestPath.getPath(this.source, this.target);
        System.out.println("Dijkstra path length: " + path.getLength());
    }
}

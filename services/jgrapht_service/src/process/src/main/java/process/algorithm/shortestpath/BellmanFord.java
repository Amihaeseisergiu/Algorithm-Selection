package process.algorithm.shortestpath;

import org.jgrapht.Graph;
import org.jgrapht.GraphPath;
import org.jgrapht.alg.shortestpath.BellmanFordShortestPath;
import org.jgrapht.graph.DefaultEdge;
import process.algorithm.Algorithm;
import process.instance.Instance;

public class BellmanFord extends Algorithm {
    String source;
    String target;
    Graph<String, DefaultEdge> graph;

    public BellmanFord(Instance instance) {
        super(instance);
        this.graph = instance.graph();
        this.source = instance.parameters().get("source").toString();
        this.target = instance.parameters().get("target").toString();
    }

    public void run() {
        BellmanFordShortestPath<String, DefaultEdge> bellmanFordShortestPath = new BellmanFordShortestPath<>(this.graph);
        GraphPath<String, DefaultEdge> path = bellmanFordShortestPath.getPath(this.source, this.target);
        System.out.println("Bellmanford path length: " + path.getLength());
    }
}

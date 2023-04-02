package process.algorithm.shortestpath;

import org.jgrapht.Graph;
import org.jgrapht.GraphPath;
import org.jgrapht.alg.shortestpath.AStarShortestPath;
import org.jgrapht.graph.DefaultEdge;
import process.algorithm.Algorithm;
import process.instance.Instance;

public class AStar extends Algorithm {
    String source;
    String target;
    Graph<String, DefaultEdge> graph;

    public AStar(Instance instance) {
        super(instance);
        this.graph = instance.graph();
        this.source = instance.parameters().get("source").toString();
        this.target = instance.parameters().get("target").toString();
    }

    public void run() {
        AStarShortestPath<String, DefaultEdge> aStarShortestPath =
                new AStarShortestPath<>(this.graph, (sourceVertex, targetVertex) -> 0);
        GraphPath<String, DefaultEdge> path = aStarShortestPath.getPath(this.source, this.target);
        System.out.println("AStar path length: " + path.getLength());
    }
}

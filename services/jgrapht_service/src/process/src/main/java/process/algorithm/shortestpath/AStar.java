package process.algorithm.shortestpath;

import org.jgrapht.GraphPath;
import org.jgrapht.alg.shortestpath.AStarShortestPath;
import org.jgrapht.graph.DefaultEdge;
import process.algorithm.Algorithm;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.List;

public class AStar extends Algorithm {
    int source;
    int target;

    public AStar(Instance instance, List<Publisher> publishers) {
        super(instance, publishers);
        this.source = parameters.get("source").toInt();
        this.target = parameters.get("target").toInt();
    }

    public void algorithm() {
        AStarShortestPath<Integer, DefaultEdge> aStarShortestPath =
                new AStarShortestPath<>(this.graph, (sourceVertex, targetVertex) -> 0);
        GraphPath<Integer, DefaultEdge> path = aStarShortestPath.getPath(this.source, this.target);

        bestResult = path.getLength();
    }
}

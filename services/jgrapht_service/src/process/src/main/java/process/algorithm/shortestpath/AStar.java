package process.algorithm.shortestpath;

import org.jgrapht.Graph;
import org.jgrapht.alg.shortestpath.AStarShortestPath;
import org.jgrapht.graph.DefaultEdge;
import process.algorithm.Algorithm;
import process.instance.Instance;
import process.instance.InstanceRepository;

public class AStar extends Algorithm {
    String source;
    String target;

    public AStar(Instance instance) {
        super(instance);
        this.source = instance.parameters().get("source").getAsString();
        this.target = instance.parameters().get("source").getAsString();
    }

    public void run() {
        Graph<String, DefaultEdge> graph = InstanceRepository.getGraph(this.instance);
        AStarShortestPath<String, DefaultEdge> aStarShortestPath =
                new AStarShortestPath<>(graph, (sourceVertex, targetVertex) -> 0);
        aStarShortestPath.getPath(this.source, this.target);
    }
}

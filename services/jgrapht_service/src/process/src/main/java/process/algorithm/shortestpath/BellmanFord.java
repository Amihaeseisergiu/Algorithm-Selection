package process.algorithm.shortestpath;

import org.jgrapht.Graph;
import org.jgrapht.alg.shortestpath.BellmanFordShortestPath;
import org.jgrapht.graph.DefaultEdge;
import process.algorithm.Algorithm;
import process.instance.Instance;
import process.instance.InstanceRepository;

public class BellmanFord extends Algorithm {

    String source;
    String target;

    public BellmanFord(Instance instance) {
        super(instance);
        this.source = instance.parameters().get("source").getAsString();
        this.target = instance.parameters().get("source").getAsString();
    }

    public void run() {
        Graph<String, DefaultEdge> graph = InstanceRepository.getGraph(this.instance);
        BellmanFordShortestPath<String, DefaultEdge> bellmanFordShortestPath = new BellmanFordShortestPath<>(graph);
        bellmanFordShortestPath.getPath(this.source, this.target);
    }
}

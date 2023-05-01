package process.algorithm;

import lombok.RequiredArgsConstructor;
import process.algorithm.coloring.DSatur;
import process.algorithm.coloring.TabuCol;
import process.algorithm.shortestpath.FloydWarshall;
import process.algorithm.shortestpath.BellmanFord;
import process.algorithm.shortestpath.Dijkstra;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.List;

@RequiredArgsConstructor
public class Algorithms {

    private final Instance instance;
    private final List<Publisher> publishers;

    public Algorithm getAlgorithm(String algorithmName) throws Exception {
        switch (algorithmName) {
            case "Dijkstra":
                return new Dijkstra(instance, publishers);
            case "Bellman-Ford":
                return new BellmanFord(instance, publishers);
            case "Floyd-Warshall":
                return new FloydWarshall(instance, publishers);
            case "DSatur":
                return new DSatur(instance, publishers);
            case "TabuCol":
                return new TabuCol(instance, publishers);
            default:
                throw new Exception("Algorithm not implemented");
        }
    }
}

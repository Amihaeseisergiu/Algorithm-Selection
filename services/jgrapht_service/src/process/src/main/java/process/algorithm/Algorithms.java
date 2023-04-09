package process.algorithm;

import process.algorithm.shortestpath.AStar;
import process.algorithm.shortestpath.BellmanFord;
import process.algorithm.shortestpath.Dijkstra;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.List;
import java.util.Map;

import static java.util.Map.entry;

public class Algorithms {

    public static Map<String, Algorithm> getMapping(Instance instance, List<Publisher> publishers) {
        return Map.ofEntries(
                entry("Dijkstra", new Dijkstra(instance, publishers)),
                entry("A*", new AStar(instance, publishers)),
                entry("Bellman-Ford", new BellmanFord(instance, publishers))
        );
    }
}

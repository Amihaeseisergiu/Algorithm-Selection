package process.algorithm;

import process.algorithm.shortestpath.FloydWarshall;
import process.algorithm.shortestpath.BellmanFord;
import process.algorithm.shortestpath.Dijkstra;
import process.instance.Instance;

import java.util.Map;
import static java.util.Map.entry;

public class Algorithms {

    public static Map<String, Algorithm> getMapping(Instance instance) {
        return Map.ofEntries(
                entry("dijkstra", new Dijkstra(instance)),
                entry("floydwarshall", new FloydWarshall(instance)),
                entry("bellmanford", new BellmanFord(instance))
        );
    }
}

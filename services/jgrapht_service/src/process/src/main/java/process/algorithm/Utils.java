package process.algorithm;

import org.jgrapht.Graph;
import org.jgrapht.alg.clique.BronKerboschCliqueFinder;
import org.jgrapht.graph.DefaultEdge;

import java.util.Set;

public class Utils {
    public static int largestClique(Graph<Integer, DefaultEdge> graph) {
        BronKerboschCliqueFinder<Integer, DefaultEdge> cliqueFinder = new BronKerboschCliqueFinder<>(graph);
        int maxCliqueSize = 0;

        for (Set<Integer> clique : cliqueFinder) {
            if (clique.size() > maxCliqueSize) {
                maxCliqueSize = clique.size();
            }
        }

        return maxCliqueSize;
    }
}

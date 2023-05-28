package process.algorithm.coloring;

import org.jgrapht.alg.color.BrownBacktrackColoring;
import org.jgrapht.graph.DefaultEdge;
import process.algorithm.Algorithm;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.List;

public class ColoringBacktrack extends Algorithm {

    public ColoringBacktrack(Instance instance, List<Publisher> publishers) {
        super(instance, publishers);
    }

    public void algorithm() {
        try {
            BrownBacktrackColoring<Integer, DefaultEdge> brownBacktrackColoring = new BrownBacktrackColoring<>(this.graph);

            bestResult = brownBacktrackColoring.getColoring().getNumberColors();
        } catch (Exception e) {
            e.printStackTrace();
            throw e;
        }
    }
}

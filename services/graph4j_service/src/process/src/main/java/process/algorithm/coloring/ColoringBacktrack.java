package process.algorithm.coloring;

import org.graph4j.alg.coloring.BacktrackColoring;
import process.algorithm.Algorithm;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.List;

public class ColoringBacktrack extends Algorithm {

    public ColoringBacktrack(Instance instance, List<Publisher> publishers) {
        super(instance, publishers);
    }

    public void algorithm() {
        BacktrackColoring backtrackColoring = new BacktrackColoring(
                this.graph, Integer.parseInt(System.getenv("ALGORITHM_TIMEOUT")) * 1000);

        bestResult = backtrackColoring.findColoring().numUsedColors();
    }
}

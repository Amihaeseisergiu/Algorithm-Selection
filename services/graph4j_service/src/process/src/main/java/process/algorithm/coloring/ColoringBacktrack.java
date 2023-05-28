package process.algorithm.coloring;

import org.graph4j.alg.coloring.exact.ParallelBacktrackColoring;
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
            ParallelBacktrackColoring backtrackColoring = new ParallelBacktrackColoring(
                    this.graph, Integer.parseInt(System.getenv("ALGORITHM_TIMEOUT")) * 1000L);

            bestResult = backtrackColoring.findColoring().numUsedColors();
        } catch (Exception e) {
            e.printStackTrace();
            throw e;
        }
    }
}

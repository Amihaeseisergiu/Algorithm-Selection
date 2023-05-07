package process.algorithm.coloring;

import org.graph4j.alg.coloring.DSaturGreedyColoring;
import process.algorithm.Algorithm;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.List;

public class DSatur extends Algorithm {

    public DSatur(Instance instance, List<Publisher> publishers) {
        super(instance, publishers);
    }

    public void algorithm() {
        DSaturGreedyColoring dSaturGreedyColoring = new DSaturGreedyColoring(this.graph);

        bestResult = dSaturGreedyColoring.findColoring().numUsedColors();
    }
}

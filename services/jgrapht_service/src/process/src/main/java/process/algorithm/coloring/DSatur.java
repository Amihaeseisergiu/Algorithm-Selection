package process.algorithm.coloring;

import org.jgrapht.alg.color.SaturationDegreeColoring;
import org.jgrapht.graph.DefaultEdge;
import process.algorithm.Algorithm;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.List;

public class DSatur extends Algorithm {

    public DSatur(Instance instance, List<Publisher> publishers) {
        super(instance, publishers);
    }

    public double algorithm() {
        SaturationDegreeColoring<String, DefaultEdge> saturationDegreeColoring = new SaturationDegreeColoring<>(this.graph);
        int numberOfColors = saturationDegreeColoring.getColoring().getNumberColors();

        return numberOfColors;
    }
}
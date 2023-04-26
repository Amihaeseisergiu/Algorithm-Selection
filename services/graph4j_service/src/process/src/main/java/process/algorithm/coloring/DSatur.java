package process.algorithm.coloring;

import process.algorithm.Algorithm;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.HashMap;
import java.util.List;

public class DSatur extends Algorithm {

    private final HashMap<Integer, Integer> colorMap;

    public DSatur(Instance instance, List<Publisher> publishers) {
        super(instance, publishers);
        this.colorMap = new HashMap<>();
    }

    public double algorithm() {
        int n = graph.numVertices();
        int[] vertices = new int[n];

        for (int i = 0; i < n; i++) {
            vertices[i] = i;
        }

        int maxDegree = 0;
        int maxDegreeVertex = 0;
        for (int i = 0; i < n; i++) {
            int degree = graph.degree(i);
            if (degree > maxDegree) {
                maxDegree = degree;
                maxDegreeVertex = i;
            }
        }

        colorMap.put(maxDegreeVertex, 0);
        vertices[maxDegreeVertex] = -1;
        int verticesColored = 1;
        int numberOfColors = 0;

        while (verticesColored < n) {
            int maxSaturationDegree = -1;
            int selectedVertex = -1;
            int selectedColor = -1;

            for (int i = 0; i < n; i++) {
                if (vertices[i] != -1) {
                    int vertex = vertices[i];

                    int saturationDegree = 0;
                    int[] neighbors = graph.neighbors(vertex);
                    HashMap<Integer, Integer> usedColors = new HashMap<>();

                    for (int neighbor : neighbors) {
                        if (colorMap.containsKey(neighbor)) {
                            int color = colorMap.get(neighbor);
                            usedColors.put(color, 1);
                        }
                    }

                    saturationDegree = usedColors.size();
                    if (saturationDegree > maxSaturationDegree || (saturationDegree == maxSaturationDegree && graph.degree(vertex) > graph.degree(selectedVertex))) {
                        maxSaturationDegree = saturationDegree;
                        selectedVertex = vertex;
                    }
                }
            }

            int[] neighbors = graph.neighbors(selectedVertex);
            HashMap<Integer, Integer> usedColors = new HashMap<>();

            for (int neighbor : neighbors) {
                if (colorMap.containsKey(neighbor)) {
                    int color = colorMap.get(neighbor);
                    usedColors.put(color, 1);
                }
            }

            for (int i = 0; i < n; i++) {
                if (!usedColors.containsKey(i)) {
                    selectedColor = i;
                    break;
                }
            }

            colorMap.put(selectedVertex, selectedColor);
            numberOfColors = Math.max(numberOfColors, selectedColor);

            vertices[selectedVertex] = -1;
            verticesColored += 1;
        }

        return numberOfColors + 1;
    }
}

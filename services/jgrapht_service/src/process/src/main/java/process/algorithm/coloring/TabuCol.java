package process.algorithm.coloring;

import org.jgrapht.Graph;
import org.jgrapht.Graphs;
import org.jgrapht.alg.color.SaturationDegreeColoring;
import org.jgrapht.alg.util.Pair;
import org.jgrapht.graph.DefaultEdge;
import process.algorithm.Algorithm;
import process.algorithm.Utils;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Set;

public class TabuCol extends Algorithm {

    public TabuCol(Instance instance, List<Publisher> publishers) {
        super(instance, publishers);
    }

    public void algorithm() {
        int lowerBound = Utils.largestClique(graph);
        int upperBound = new SaturationDegreeColoring<>(this.graph).getColoring().getNumberColors();
        bestResult = upperBound;

        for (int numberOfColors = upperBound - 1; numberOfColors >= lowerBound; numberOfColors--) {
            System.out.println("Trying with " + numberOfColors + "/" + upperBound + " colors");
            if (tabucol(this.graph, numberOfColors, 10, 10, 100, false) == null) {
                bestResult = numberOfColors + 1;
                break;
            }
        }
    }

    private Map<Integer, Integer> tabucol(Graph<Integer, DefaultEdge> graph, int numberOfColors,
                                                int tabuSize, int reps, int maxIterations, boolean debug) {
        try {
            // nodes are represented with indices, [0, 1, ..., n-1]
            // colors are represented by numbers, [0, 1, ..., k-1]
            List<Integer> colors = new ArrayList<>();

            for (int i = 0; i < numberOfColors; i++) {
                colors.add(i);
            }

            // number of iterations of the tabucol algorithm
            int iterations = 0;

            // initialize tabu as an empty deque
            Deque<Pair<Integer, Integer>> tabu = new ArrayDeque<>();

            // solution is a map of nodes to colors
            // generate initial random solution
            Map<Integer, Integer> solution = new HashMap<>();
            Random rand = new Random();
            for (int i: graph.vertexSet()) {
                solution.put(i, colors.get(rand.nextInt(numberOfColors)));
            }

            // aspiration level A(z), represented by a mapping: f(s) -> best f(s') seen so far
            Map<Integer, Integer> aspirationLevel = new HashMap<>();
            int conflictCount = 0;

            while (iterations < maxIterations) {
                // Count node pairs (i,j) which are adjacent and have the same color.
                Set<Integer> moveCandidates = new HashSet<>(); // use a set to avoid duplicates
                conflictCount = 0;

                for (int i : graph.vertexSet()) { // assume undirected graph, ignoring self-loops
                    for (int j : Graphs.neighborListOf(graph, i)) {
                        if (solution.get(i).equals(solution.get(j))) { // same color
                            moveCandidates.add(i);
                            moveCandidates.add(j);
                            conflictCount++;
                        }
                    }
                }

                // convert to list for array indexing
                List<Integer> moveCandidatesList = new ArrayList<>(moveCandidates);

                if (conflictCount == 0) {
                    // found a valid coloring
                    break;
                }

                // generate neighboring solutions
                Map<Integer, Integer> newSolution = null;
                int node = 0;

                for (int r = 0; r < reps; r++) {
                    // choose a random node to move to
                    node = moveCandidatesList.get(rand.nextInt(moveCandidatesList.size()));
                    int newColor = colors.get(rand.nextInt(numberOfColors - 1));

                    if (solution.get(node) == newColor) {
                        // essentially swapping last color with current color for this calculation
                        newColor = colors.get(numberOfColors - 1);
                    }

                    // create a neighboring solution
                    newSolution = new HashMap<>(solution);
                    newSolution.put(node, newColor);

                    // Count adjacent pairs with the same color in the new solution.
                    int newConflicts = 0;

                    for (int i : graph.vertexSet()) {
                        for (int j : Graphs.neighborListOf(graph, i)) {
                            if (newSolution.get(i).equals(newSolution.get(j))) {
                                newConflicts++;
                            }
                        }
                    }

                    // found an improved solution
                    if (newConflicts < conflictCount) {
                        // if f(s') <= A(f(s)) [where A(z) defaults to z - 1]
                        if (newConflicts <= aspirationLevel.getOrDefault(conflictCount, conflictCount - 1)) {
                            // set A(f(s) = f(s') - 1
                            aspirationLevel.put(conflictCount, newConflicts - 1);

                            // permit tabu move if it is better any prior
                            if (tabu.contains(new Pair<>(node, newColor))) {
                                tabu.remove(new Pair<>(node, newColor));
                                if (debug) {
                                    System.out.println("tabu permitted; " + conflictCount + " -> " + newConflicts);
                                }
                                break;
                            }
                        } else {
                            if (tabu.contains(new Pair<>(node, newColor))) {
                                // tabu move isn't good enough
                                continue;
                            }
                        }

                        if (debug) {
                            System.out.println(conflictCount + " -> " + newConflicts);
                        }

                        if (newConflicts < bestHeuristicScore) {
                            bestHeuristicScore = newConflicts;
                        }

                        break;
                    }
                }

                if (newSolution == null) {
                    break;
                }

                // At this point, either found a better solution,
                // or ran out of reps, using the last solution generated

                // The current node color will become tabu.
                // add to the end of the tabu queue

                tabu.offer(new Pair<>(node, solution.get(node)));
                if (tabu.size() > tabuSize) {
                    tabu.poll();
                }

                solution = new HashMap<>(newSolution);
                iterations++;
                if (debug && iterations % 500 == 0) {
                    System.out.println("Iteration: " + iterations);
                }
            }

            if (conflictCount != 0) {
                System.out.println("No coloring found with " + numberOfColors + " colors");
                return null;
            } else {
                System.out.println("Found coloring: " + solution);
                bestHeuristicScore = 0;
                return solution;
            }
        } catch (Exception e) {
            e.printStackTrace();
            throw e;
        }
    }
}

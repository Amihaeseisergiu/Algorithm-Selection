package process.algorithm.coloring;

import org.graph4j.alg.clique.MaximalCliqueFinder;
import org.graph4j.alg.coloring.DSaturGreedyColoring;
import process.algorithm.Algorithm;
import process.instance.Instance;
import process.pubsub.Publisher;

import java.util.List;
import java.util.Random;

public class ColoringGeneticAlgorithm extends Algorithm {
    Random random = new Random();

    public ColoringGeneticAlgorithm(Instance instance, List<Publisher> publishers) {
        super(instance, publishers);
    }

    public void algorithm() {
        int lowerBound = new MaximalCliqueFinder(this.graph).getMaximalClique().size();
        int upperBound = new DSaturGreedyColoring(this.graph).findColoring().numUsedColors();
        bestResult = upperBound;

        for (int numberOfColors = upperBound - 1; numberOfColors >= lowerBound; numberOfColors--) {
            System.out.println("GACol Trying with " + numberOfColors + "/" + upperBound + " colors");
            if (geneticAlgorithm(100, 10, numberOfColors, 0.9, 0.9) == null) {
                bestResult = numberOfColors + 1;
                break;
            }
        }
    }

    private int[] geneticAlgorithm(int maxGenerations, int populationSize, int numberOfColors,
                                   double crossoverProbability, double mutationRate) {
        int[][] population = new int[populationSize][graph.numVertices()];
        double[] fitness = new double[population.length];

        int bestSolutionIndex = -1;
        double bestFitness = 0.0;
        double totalFitness = 0.0;

        // Initial initialization and evaluation of the population
        for (int i = 0; i < populationSize; i++) {
            for (int j = 0; j < graph.numVertices(); j++) {
                population[i][j] = random.nextInt(numberOfColors);
            }

            int conflicts = getConflicts(population[i]);
            fitness[i] = getFitness(conflicts);
            totalFitness += fitness[i];

            if (fitness[i] > bestFitness) {
                bestSolutionIndex = i;
                bestFitness = fitness[i];
                bestHeuristicScore = conflicts;
            }
        }

        int generation = 0;
        int numberOfIterationsWithoutChange = 0;

        while (generation < maxGenerations && bestFitness < 1.0) {
            // Selection
            int[][] newPopulation = new int[population.length][population[0].length];

            for (int newChromosome = 0; newChromosome < population.length; newChromosome++) {
                double r = random.nextDouble() * totalFitness;
                int oldChromosome = 0;
                double fitnessSum = fitness[0];

                while (fitnessSum < r) {
                    oldChromosome++;
                    fitnessSum += fitness[oldChromosome];
                }

                for (int gene = 0; gene < population[0].length; gene++) {
                    newPopulation[newChromosome][gene] = population[oldChromosome][gene];
                }
            }

            population = newPopulation;

            // Crossover
            int firstChromosome = -1;
            for (int currentChromosome = 0; currentChromosome < population.length; currentChromosome++) {
                if (random.nextDouble() < crossoverProbability) {
                    if (firstChromosome != -1) {
                        int crossoverPoint = random.nextInt(population[0].length);

                        for (int j = 0; j < crossoverPoint; j++) {
                            int aux = population[firstChromosome][j];
                            population[firstChromosome][j] = population[currentChromosome][j];
                            population[currentChromosome][j] = aux;
                        }

                        firstChromosome = -1;
                    } else {
                        firstChromosome = currentChromosome;
                    }
                }
            }

            // Mutation
            for (int i = 0; i < population.length; i++) {
                for (int j = 0; j < population[0].length; j++) {
                    if (random.nextDouble() < mutationRate) {
                        population[i][j] = random.nextInt(numberOfColors);
                    }
                }
            }

            // Evaluation
            totalFitness = 0.0;
            boolean bestFitnessChanged = false;

            for (int i = 0; i < populationSize; i++) {
                int conflicts = getConflicts(population[i]);
                fitness[i] = getFitness(conflicts);
                totalFitness += fitness[i];

                if (fitness[i] > bestFitness) {
                    bestSolutionIndex = i;
                    bestFitness = fitness[i];
                    bestHeuristicScore = conflicts;
                    bestFitnessChanged = true;
                }
            }

            if (!bestFitnessChanged) {
                numberOfIterationsWithoutChange++;
            }

            if (numberOfIterationsWithoutChange > 0 && numberOfIterationsWithoutChange % 10 == 0) {
                mutationRate *= 0.99;
                crossoverProbability *= 0.99;
            }

            // System.out.println("Generation " + generation + ": best solution has " + bestFitness + ", total " + totalFitness);
            generation++;
        }

        if (bestFitness < 1.0) {
            System.out.println("No coloring found with " + numberOfColors + " colors");
            return null;
        } else {
            System.out.println("Found coloring in " + generation + " generations");
            bestHeuristicScore = 0;
            return population[bestSolutionIndex];
        }
    }

    private int getConflicts(int[] coloring) {
        int conflicts = 0;

        for (int i : graph.vertices()) {
            for (int j : graph.neighbors(i)) {
                if (coloring[i] == coloring[j]) {
                    conflicts++;
                }
            }
        }

        return conflicts;
    }

    private double getFitness(int conflicts) {
        return 1.0 / (conflicts + 1);
    }
}
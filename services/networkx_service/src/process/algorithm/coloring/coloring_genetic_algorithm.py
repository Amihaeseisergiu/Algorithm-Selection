import random
import numpy as np
import networkx as nx
from networkx.algorithms import approximation
from algorithm.algorithm import Algorithm

class ColoringGeneticAlgorithm(Algorithm):
    def __init__(self, instance, publishers):
        super().__init__(instance, publishers)

    def algorithm(self):
        lower_bound = len(approximation.max_clique(self.graph))
        upper_bound = max(nx.coloring.greedy_color(self.graph, strategy="DSATUR").values()) + 1
        self.best_result = upper_bound

        for n_colors in range(upper_bound - 1, lower_bound, -1):
            print(f"CGA Trying with {n_colors}/{upper_bound} colors", flush=True)
            if self.genetic_algorithm(100, 10, n_colors, 0.9, 0.9) is None:
                self.best_result = n_colors + 1
                break

    def genetic_algorithm(self, max_generations, population_size, num_colors, crossover_probability, mutation_rate):
        population = np.zeros((population_size, len(self.graph)), dtype=int)
        fitness = np.zeros(population_size)

        best_solution_index = -1
        best_fitness = 0.0
        total_fitness = 0.0

        # Initial initialization and evaluation of the population
        for i in range(population_size):
            for j in range(len(self.graph)):
                population[i][j] = random.randint(0, num_colors - 1)

            conflicts = self.get_conflicts(population[i])
            fitness[i] = self.get_fitness(conflicts)
            total_fitness += fitness[i]

            if fitness[i] > best_fitness:
                best_solution_index = i
                best_fitness = fitness[i]
                self.best_heuristic_score = conflicts

        generation = 0
        num_iterations_without_change = 0

        while generation < max_generations and best_fitness < 1.0:
            # Selection
            new_population = np.zeros((population_size, population.shape[1]), dtype=int)

            for new_chromosome in range(population_size):
                r = random.random() * total_fitness
                old_chromosome = 0
                fitness_sum = fitness[0]

                while fitness_sum < r:
                    old_chromosome += 1
                    fitness_sum += fitness[old_chromosome]

                for gene in range(population.shape[1]):
                    new_population[new_chromosome][gene] = population[old_chromosome][gene]

            population = new_population

            # Crossover
            first_chromosome = -1
            for current_chromosome in range(population_size):
                if random.random() < crossover_probability:
                    if first_chromosome != -1:
                        crossover_point = random.randint(0, population.shape[1] - 1)

                        for j in range(crossover_point):
                            aux = population[first_chromosome][j]
                            population[first_chromosome][j] = population[current_chromosome][j]
                            population[current_chromosome][j] = aux

                        first_chromosome = -1
                    else:
                        first_chromosome = current_chromosome

            # Mutation
            for i in range(population_size):
                for j in range(population.shape[1]):
                    if random.random() < mutation_rate:
                        population[i][j] = random.randint(0, num_colors - 1)

            # Evaluation
            total_fitness = 0.0
            best_fitness_changed = False

            for i in range(population_size):
                conflicts = self.get_conflicts(population[i])
                fitness[i] = self.get_fitness(conflicts)
                total_fitness += fitness[i]

                if fitness[i] > best_fitness:
                    best_solution_index = i
                    best_fitness = fitness[i]
                    self.best_heuristic_score = conflicts
                    best_fitness_changed = True

            if not best_fitness_changed:
                num_iterations_without_change += 1

            if num_iterations_without_change > 0 and num_iterations_without_change % 10 == 0:
                mutation_rate *= 0.99
                crossover_probability *= 0.99

            generation += 1

        if best_fitness < 1.0:
            print("No coloring found with " + str(num_colors) + " colors", flush=True)
            return None
        else:
            print("Found coloring in " + str(generation) + " generations", flush=True)
            self.best_heuristic_score = 0
            return population[best_solution_index]

    def get_conflicts(self, coloring):
        conflicts = 0

        for index1, node1 in enumerate(self.graph.nodes()):
            for node2 in self.graph.neighbors(node1):
                index2 = list(self.graph.nodes()).index(node2)

                if coloring[index1] == coloring[index2]:
                    conflicts += 1

        return conflicts

    def get_fitness(self, conflicts):
        return 1.0 / (conflicts + 1)

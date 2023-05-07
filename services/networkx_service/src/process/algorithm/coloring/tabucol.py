import networkx as nx
from algorithm.algorithm import Algorithm
from collections import deque
from random import randrange
from networkx.algorithms import approximation


class TabuCol(Algorithm):
    def __init__(self, instance, publishers):
        super().__init__(instance, publishers)

    def algorithm(self):
        lower_bound = len(approximation.max_clique(self.graph))
        upper_bound = max(nx.coloring.greedy_color(self.graph, strategy="DSATUR").values()) + 1
        self.best_result = upper_bound

        for n_colors in range(upper_bound - 1, lower_bound, -1):
            print(f"TabuCol Trying with {n_colors}/{upper_bound} colors", flush=True)
            if not self.tabucol(self.graph, n_colors, debug=False):
                self.best_result = n_colors + 1
                break

    def tabucol(self, graph, number_of_colors, tabu_size=10, reps=10, max_iterations=100, debug=False):
        # nodes are represented with indices, [0, 1, ..., n-1]
        # colors are represented by numbers, [0, 1, ..., k-1]
        colors = list(range(number_of_colors))
        # number of iterations of the tabucol algorithm
        iterations = 0
        # initialize tabu as empty queue
        tabu = deque()

        # solution is a map of nodes to colors
        # Generate a random solution:
        solution = dict()
        for i in range(len(graph)):
            solution[i] = colors[randrange(0, len(colors))]

        # Aspiration level A(z), represented by a mapping: f(s) -> best f(s') seen so far
        aspiration_level = dict()

        conflict_count = 0

        while iterations < max_iterations:
            # Count node pairs (i,j) which are adjacent and have the same color.
            move_candidates = set()  # use a set to avoid duplicates
            conflict_count = 0
            for i in range(len(graph)):
                for j in graph.neighbors(i):  # assume undirected graph, ignoring self-loops
                    if solution[i] == solution[j]:  # same color
                        move_candidates.add(i)
                        move_candidates.add(j)
                        conflict_count += 1

            move_candidates = list(move_candidates)  # convert to list for array indexing

            if conflict_count == 0:
                # Found a valid coloring.
                break

            # Generate neighbor solutions.
            new_solution = None
            node = None
            for r in range(reps):
                # Choose a node to move.
                node = move_candidates[randrange(0, len(move_candidates))]

                # Choose color other than current.
                new_color = colors[randrange(0, len(colors) - 1)]
                if solution[node] == new_color:
                    # essentially swapping last color with current color for this calculation
                    new_color = colors[-1]

                # Create a neighbor solution
                new_solution = solution.copy()
                new_solution[node] = new_color

                # Count adjacent pairs with the same color in the new solution.
                new_conflicts = 0

                for i in range(len(graph)):
                    for j in graph.neighbors(i):
                        if new_solution[i] == new_solution[j]:
                            new_conflicts += 1

                if new_conflicts < conflict_count:  # found an improved solution
                    # if f(s') <= A(f(s)) [where A(z) defaults to z - 1]
                    if new_conflicts <= aspiration_level.setdefault(conflict_count, conflict_count - 1):
                        # set A(f(s) = f(s') - 1
                        aspiration_level[conflict_count] = new_conflicts - 1

                        if (node, new_color) in tabu:  # permit tabu move if it is better any prior
                            tabu.remove((node, new_color))
                            if debug:
                                print(f"Tabu permitted; {conflict_count} -> {new_conflicts}", flush=True)
                            break
                    else:
                        if (node, new_color) in tabu:
                            # tabu move isn't good enough
                            continue
                    if debug:
                        print(f"{conflict_count} -> {new_conflicts}", flush=True)

                    if new_conflicts < self.best_heuristic_score:
                        self.best_heuristic_score = new_conflicts

                    break

            # At this point, either found a better solution,
            # or ran out of reps, using the last solution generated

            # The current node color will become tabu.
            # add to the end of the tabu queue
            tabu.append((node, solution[node]))
            if len(tabu) > tabu_size:  # queue full
                tabu.popleft()  # remove the oldest move

            # Move to next iteration of tabucol with new solution
            solution = new_solution
            iterations += 1

            if debug and iterations % 500 == 0:
                print(f"Iteration: {iterations}", flush=True)

        # print("Aspiration Levels:\n" + "\n".join([str((k,v)) for k,v in aspiration_level.items() if k-v > 1]))

        # At this point, either conflict_count is 0 and a coloring was found,
        # or ran out of iterations with no valid coloring.
        if conflict_count != 0:
            print(f"No coloring found with {number_of_colors} colors \n", flush=True)
            return None
        else:
            print(f"Found coloring: {solution}\n", flush=True)
            self.best_heuristic_score = 0
            return solution

import networkx as nx
from networkx.algorithms import approximation
from algorithm.algorithm import Algorithm


class ColoringBacktrack(Algorithm):
    def __init__(self, instance, publishers):
        super().__init__(instance, publishers)

    def algorithm(self):
        lower_bound, upper_bound = len(approximation.max_clique(self.graph)),\
            max(nx.coloring.greedy_color(self.graph, strategy="DSATUR").values()) + 1
        self.best_result = upper_bound

        while lower_bound <= upper_bound:
            number_of_colors = (lower_bound + upper_bound) // 2

            try:
                colors = self.backtrack_coloring(number_of_colors)
            except Exception:
                break

            if colors:
                upper_bound = number_of_colors - 1
            else:
                lower_bound = number_of_colors + 1

        self.best_result = lower_bound

    def backtrack_coloring(self, num_colors):
        color_map = {}
        nodes = list(self.graph.nodes())

        def is_valid(node, color):
            for neighbor in self.graph.neighbors(node):
                if neighbor in color_map and color_map[neighbor] == color:
                    return False
            return True

        def backtrack(node_idx):
            if node_idx == len(nodes):
                return True

            node = nodes[node_idx]

            for color in range(num_colors):
                if is_valid(node, color):
                    color_map[node] = color

                    if backtrack(node_idx + 1):
                        return True

                    del color_map[node]

            return False

        if backtrack(0):
            return color_map
        else:
            return None

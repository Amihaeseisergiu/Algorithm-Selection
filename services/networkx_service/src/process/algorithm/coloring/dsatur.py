import networkx as nx
from algorithm.algorithm import Algorithm


class DSatur(Algorithm):
    def __init__(self, instance, publishers):
        super().__init__(instance, publishers)

    def algorithm(self):
        color_map = nx.coloring.greedy_color(self.graph, strategy="DSATUR")
        num_colors = max(color_map.values()) + 1

        return num_colors

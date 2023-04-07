import networkx as nx
from algorithm.algorithm import Algorithm


class BellmanFord(Algorithm):
    def __init__(self, instance, publishers):
        super().__init__(instance, publishers)
        self.source = self.parameters['source']
        self.target = self.parameters['target']

    def algorithm(self):
        path = nx.bellman_ford_path(self.graph, int(self.source), int(self.target))

        return len(path) - 1

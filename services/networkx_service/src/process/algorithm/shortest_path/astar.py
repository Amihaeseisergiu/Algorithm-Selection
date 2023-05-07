import networkx as nx
from algorithm.algorithm import Algorithm


class AStar(Algorithm):
    def __init__(self, instance, publishers):
        super().__init__(instance, publishers)
        self.source = self.parameters['source']
        self.target = self.parameters['target']

    def algorithm(self):
        path = nx.astar_path(self.graph, int(self.source), int(self.target))

        self.best_result = len(path) - 1

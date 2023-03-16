import networkx as nx
from algorithm.algorithm import Algorithm


class Astar(Algorithm):
    def __init__(self, socket_id):
        super().__init__(socket_id, "A*", self.algorithm)

    def algorithm(self, data):
        graph = nx.node_link_graph(data['graph'])
        source = data['source']
        target = data['target']

        nx.astar_path(graph, source, target)

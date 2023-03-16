import networkx as nx
from algorithm.algorithm import Algorithm


class BellmanFord(Algorithm):
    def __init__(self, socket_id):
        super().__init__(socket_id, "Bellman-Ford", self.algorithm)

    def algorithm(self, data):
        graph = nx.node_link_graph(data['graph'])
        source = data['source']
        target = data['target']

        nx.bellman_ford_path(graph, source, target)

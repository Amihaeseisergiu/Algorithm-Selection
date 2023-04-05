import networkx as nx
from algorithm.algorithm import Algorithm


class Dijkstra(Algorithm):
    def __init__(self, instance, algorithm_name, file_id):
        super().__init__(instance, algorithm_name, file_id)
        self.graph = instance.graph
        self.source = instance.parameters['source']
        self.target = instance.parameters['target']

    def run(self):
        path = nx.dijkstra_path(self.graph, int(self.source), int(self.target))
        print(f"Dijkstra path length: {len(path)}", flush=True)

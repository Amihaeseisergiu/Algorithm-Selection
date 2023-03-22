import networkx as nx
from algorithm.algorithm import Algorithm
from instance.instance_repository import InstanceRepository


class AStar(Algorithm):
    def __init__(self, instance):
        super().__init__(instance)

    def run(self):
        graph = InstanceRepository.get_graph(self.instance)
        source = self.instance.parameters['source']
        target = self.instance.parameters['target']

        nx.astar_path(graph, int(source), int(target))

from .shortest_path.astar import AStar
from .shortest_path.bellman_ford import BellmanFord
from .shortest_path.dijkstra import Dijkstra
from .coloring.dsatur import DSatur
from .coloring.tabucol import TabuCol


class Algorithms:
    def __init__(self, instance, publishers):
        self.instance = instance
        self.publishers = publishers

    def get_algorithm(self, algorithm_name):
        match algorithm_name:
            case "Dijkstra":
                return Dijkstra(self.instance, self.publishers)
            case "Bellman-Ford":
                return BellmanFord(self.instance, self.publishers)
            case "A*":
                return AStar(self.instance, self.publishers)
            case "DSatur":
                return DSatur(self.instance, self.publishers)
            case "TabuCol":
                return TabuCol(self.instance, self.publishers)
            case _:
                raise NotImplementedError("Algorithm not implemented")

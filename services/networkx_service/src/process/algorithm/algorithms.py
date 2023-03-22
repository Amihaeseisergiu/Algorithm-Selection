from .shortest_path.astar import AStar
from .shortest_path.bellman_ford import BellmanFord
from .shortest_path.dijkstra import Dijkstra


class Algorithms:
    @staticmethod
    def get_mapping(instance):
        return {
            "dijkstra": Dijkstra(instance),
            "bellmanford": BellmanFord(instance),
            "astar": AStar(instance)
        }

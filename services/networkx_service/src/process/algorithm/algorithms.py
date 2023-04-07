from .shortest_path.astar import AStar
from .shortest_path.bellman_ford import BellmanFord
from .shortest_path.dijkstra import Dijkstra


class Algorithms:
    @staticmethod
    def get_mapping(instance, publishers):
        return {
            "Dijkstra": Dijkstra(instance, publishers),
            "Bellman-Ford": BellmanFord(instance, publishers),
            "A*": AStar(instance, publishers)
        }

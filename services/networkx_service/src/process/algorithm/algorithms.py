from .shortest_path.astar import AStar
from .shortest_path.bellman_ford import BellmanFord
from .shortest_path.dijkstra import Dijkstra


class Algorithms:
    @staticmethod
    def get_mapping(instance, algorithm_name, file_id):
        return {
            "Dijkstra": Dijkstra(instance, algorithm_name, file_id),
            "Bellman-Ford": BellmanFord(instance, algorithm_name, file_id),
            "A*": AStar(instance, algorithm_name, file_id)
        }

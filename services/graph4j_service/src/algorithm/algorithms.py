from .shortest_path.floyd_warshall import FloydWarshall
from .shortest_path.bellman_ford import BellmanFord
from .shortest_path.dijkstra import Dijkstra


class Algorithms:
    def __init__(self, socket_id, file_id):
        self.algorithm_types = {
            "shortest_path": [
                Dijkstra(socket_id, file_id, "shortest_path"),
                BellmanFord(socket_id, file_id, "shortest_path"),
                # FloydWarshall(socket_id, file_id, "shortest_path")
            ]
        }

    def get(self, algorithm_type):
        return self.algorithm_types[algorithm_type]

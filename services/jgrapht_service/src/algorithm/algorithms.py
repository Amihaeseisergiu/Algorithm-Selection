from .shortest_path.astar import AStar
from .shortest_path.bellman_ford import BellmanFord
from .shortest_path.dijkstra import Dijkstra


class Algorithms:
    def __init__(self, socket_id, file_id):
        self.algorithm_types = {
            "shortest_path": [
                Dijkstra(socket_id, file_id),
                BellmanFord(socket_id, file_id),
                AStar(socket_id, file_id)
            ]
        }

    def get(self, algorithm_type):
        return self.algorithm_types[algorithm_type]

from algorithm.shortest_path.floyd_warshall import FloydWarshall
from algorithm.shortest_path.bellman_ford import BellmanFord
from algorithm.shortest_path.dijkstra import Dijkstra
from scheduler.scheduler import AlgorithmScheduler


class ShortestPathScheduler(AlgorithmScheduler):
    def __init__(self, socket_id, file_id):
        algorithms = [
            Dijkstra(socket_id, file_id),
            BellmanFord(socket_id, file_id),
            # FloydWarshall(socket_id, file_id)
        ]

        super().__init__(socket_id=socket_id, algorithms=algorithms)

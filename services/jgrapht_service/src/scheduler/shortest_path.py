from algorithm.shortest_path.astar import Astar
from algorithm.shortest_path.bellman_ford import BellmanFord
from algorithm.shortest_path.dijkstra import Dijkstra
from scheduler.scheduler import AlgorithmScheduler


class ShortestPathScheduler(AlgorithmScheduler):
    def __init__(self, socket_id):
        algorithms = [
            Dijkstra(socket_id),
            BellmanFord(socket_id),
            Astar(socket_id)
        ]

        super().__init__(socket_id=socket_id, algorithms=algorithms)

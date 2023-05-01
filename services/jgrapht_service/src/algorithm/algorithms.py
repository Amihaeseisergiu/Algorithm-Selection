from .algorithm import Algorithm


class Algorithms:
    def __init__(self, socket_id, file_id):
        self.algorithm_types = {
            "shortest_path": [
                Algorithm(socket_id, file_id, "Dijkstra", "shortest_path"),
                Algorithm(socket_id, file_id, "Bellman-Ford", "shortest_path"),
                Algorithm(socket_id, file_id, "A*", "shortest_path")
            ],
            "coloring": [
                Algorithm(socket_id, file_id, "TabuCol", "coloring"),
                Algorithm(socket_id, file_id, "DSatur", "coloring"),
            ]
        }

    def get(self, algorithm_type):
        if algorithm_type in self.algorithm_types:
            return self.algorithm_types[algorithm_type]

        return []
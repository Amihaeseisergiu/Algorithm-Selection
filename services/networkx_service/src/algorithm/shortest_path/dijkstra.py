import subprocess
from algorithm.algorithm import Algorithm


class Dijkstra(Algorithm):
    def __init__(self, socket_id, file_id):
        algorithm_name = "Dijkstra"
        super().__init__(socket_id, file_id, algorithm_name, self.algorithm)

    def algorithm(self, instance_path):
        return subprocess.Popen(["python3", "/app/src/process/process.py",
                                 instance_path, self.algorithm_name, self.file_id])

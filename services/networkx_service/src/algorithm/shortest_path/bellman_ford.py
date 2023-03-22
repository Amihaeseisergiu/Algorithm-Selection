import subprocess
from algorithm.algorithm import Algorithm


class BellmanFord(Algorithm):
    def __init__(self, socket_id):
        super().__init__(socket_id, "Bellman-Ford", self.algorithm)

    def algorithm(self, instance_path):
        return subprocess.Popen(["python3", "/app/src/process/process.py", instance_path, "bellmanford"])

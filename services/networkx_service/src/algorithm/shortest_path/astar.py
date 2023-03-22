import subprocess
from algorithm.algorithm import Algorithm


class AStar(Algorithm):
    def __init__(self, socket_id):
        super().__init__(socket_id, "A*", self.algorithm)

    def algorithm(self, instance_path):
        return subprocess.Popen(["python3", "/app/src/process/process.py", instance_path, "astar"])

import time
import subprocess
from algorithm.algorithm import Algorithm


class BellmanFord(Algorithm):
    def __init__(self, socket_id, file_id, algorithm_type):
        algorithm_name = "Bellman-Ford"
        super().__init__(socket_id, file_id, algorithm_name, algorithm_type, self.algorithm)

    def algorithm(self, instance_path):
        return subprocess.Popen(["python3", "/app/src/process/process.py",
                                 instance_path, self.algorithm_name, self.algorithm_type,
                                 self.file_id, self.socket_id, str(time.time())])

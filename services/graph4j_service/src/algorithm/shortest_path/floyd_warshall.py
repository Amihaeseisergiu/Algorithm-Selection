import time
import subprocess
from algorithm.algorithm import Algorithm


class FloydWarshall(Algorithm):
    def __init__(self, socket_id, file_id, algorithm_type):
        algorithm_name = "Floyd-Warshall"
        super().__init__(socket_id, file_id, algorithm_name, algorithm_type, self.algorithm)

    def algorithm(self, instance_path):
        return subprocess.Popen(["java", "-jar", "-Xmx8192m", "/process/process.jar",
                                 instance_path, self.algorithm_name, self.algorithm_type,
                                 self.file_id, self.socket_id, str(time.time())])

import subprocess
from algorithm.algorithm import Algorithm


class FloydWarshall(Algorithm):
    def __init__(self, socket_id):
        super().__init__(socket_id, "Floyd Warshall", self.algorithm)

    def algorithm(self, instance_path):
        return subprocess.Popen(["java", "-jar", "-Xmx8192m", "/process/process.jar", instance_path, "floydwarshall"])

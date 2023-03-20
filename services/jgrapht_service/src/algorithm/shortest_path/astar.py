import subprocess
import networkx as nx
from algorithm.algorithm import Algorithm


class Astar(Algorithm):
    def __init__(self, socket_id):
        super().__init__(socket_id, "A*", self.algorithm)

    def algorithm(self, instance_path):
        return subprocess.Popen(["java", "-jar", "/process/process.jar", instance_path, "astar"])

import subprocess
import networkx as nx
from algorithm.algorithm import Algorithm


class Dijkstra(Algorithm):
    def __init__(self, socket_id):
        super().__init__(socket_id, "Dijkstra", self.algorithm)

    def algorithm(self, instance_path):
        return subprocess.Popen(["java", "-jar", "/process/process.jar", instance_path, "dijkstra"])

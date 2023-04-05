import json
import networkx as nx
from algorithm.algorithm import Algorithm
from network.envelope import Envelope
from pubsub.selector_algorithm_publisher import SelectorAlgorithmPublisher


class AStar(Algorithm):
    def __init__(self, instance, algorithm_name, file_id):
        super().__init__(instance, algorithm_name, file_id)
        self.graph = instance.graph
        self.source = instance.parameters['source']
        self.target = instance.parameters['target']

    def run(self):
        path = nx.astar_path(self.graph, int(self.source), int(self.target))
        print(f"A* path length: {len(path) - 1}", flush=True)

        envelope = Envelope.create_selector_envelope(self.file_id, self.algorithm_name)
        envelope["payload"] = {
            "result": len(path) - 1
        }
        SelectorAlgorithmPublisher().send(json.dumps(envelope))

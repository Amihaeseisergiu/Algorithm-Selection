import json
import networkx as nx
from .instance import Instance


class InstanceRepository:
    @staticmethod
    def get_instance(instance_path):
        with open(instance_path) as f:
            data = json.load(f)
            data_json = json.loads(data)

            return Instance(data_json['graph'], data_json['parameters'])

    @staticmethod
    def get_graph(instance):
        return nx.node_link_graph(instance.graph, link="edges")

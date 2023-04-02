import json
from .instance import Instance
from .utils import Utils


class InstanceRepository:
    @staticmethod
    def get_instance(instance_path):
        with open(instance_path) as f:
            data = json.load(f)
            data_json = json.loads(data)

            graph = Utils.construct_graph(data_json['graph'])
            parameters = data_json['parameters']

            return Instance(graph, parameters)

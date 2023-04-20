import os
import json
import networkx as nx
from .instance_repository import InstanceRepository
from pubsub.instance_features_publisher import InstanceFeaturesPublisher
from network.envelope import Envelope


class FeaturesExtractor:
    def __init__(self, file_id, algorithm_type):
        self.library_name = os.environ["LIBRARY_NAME"]
        self.file_id = file_id
        self.algorithm_type = algorithm_type
        self.instance = InstanceRepository.load_instance_file(file_id)
        self.graph = nx.node_link_graph(self.instance['graph'], link="edges")

    def extract(self):
        n_nodes = self.graph.number_of_nodes()
        n_edges = self.graph.number_of_edges()
        #density = nx.density(self.graph)

        #components = nx.connected_components(self.graph)
        #largest_component = max(components, key=len)
        #subgraph = self.graph.subgraph(largest_component)
        #diameter = nx.diameter(subgraph)

        #transitivity = nx.transitivity(self.graph)

        features = [
            n_nodes,
            n_edges,
            #density,
            #diameter,
            #transitivity
        ]

        instance_features_envelope = Envelope.create_instance_features_envelope(
            file_id=self.file_id, algorithm_type=self.algorithm_type)
        instance_features_envelope['payload']['features'] = features

        InstanceFeaturesPublisher().send(json.dumps(instance_features_envelope))

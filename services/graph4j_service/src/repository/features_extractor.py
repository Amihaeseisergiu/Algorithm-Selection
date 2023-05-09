import os
import json
import numpy as np
import networkx as nx
from .instance_repository import InstanceRepository
from pubsub.instance_features_publisher import InstanceFeaturesPublisher
from network.envelope import Envelope
from networkx.algorithms import bipartite


class FeaturesExtractor:
    def __init__(self, file_id, algorithm_type):
        self.library_name = os.environ["LIBRARY_NAME"]
        self.file_id = file_id
        self.algorithm_type = algorithm_type
        self.instance = InstanceRepository.load_instance_file(file_id)
        self.graph = nx.node_link_graph(self.instance['graph'], link="edges")

    def extract(self):
        # Graph Size Features
        n_nodes = self.graph.number_of_nodes()
        n_edges = self.graph.number_of_edges()
        ne_ratio = n_nodes / n_edges
        en_ratio = n_edges / n_nodes
        density = (2 * n_edges) / (n_nodes * (n_nodes - 1))

        # Node Degree
        degrees = np.array([d for n, d in self.graph.degree()])
        d_min = float(np.min(degrees))
        d_max = float(np.max(degrees))
        d_mean = float(np.mean(degrees))
        d_median = float(np.median(degrees))
        d_q_025 = float(np.quantile(degrees, 0.25))
        d_q_075 = float(np.quantile(degrees, 0.75))
        d_variation = float(np.std(degrees, ddof=1) / d_mean * 100)

        # Other
        is_bipartite = 1 if bipartite.is_bipartite(self.graph) else 0

        features = [
            # Graph Size Features
            n_nodes,
            n_edges,
            ne_ratio,
            en_ratio,
            density,

            # Node Degree
            d_min,
            d_max,
            d_mean,
            d_median,
            d_q_025,
            d_q_075,
            d_variation,

            # Other
            is_bipartite
        ]

        instance_features_envelope = Envelope.create_instance_features_envelope(
            file_id=self.file_id, algorithm_type=self.algorithm_type)
        instance_features_envelope['payload']['features'] = features

        InstanceFeaturesPublisher().send(json.dumps(instance_features_envelope))

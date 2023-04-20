import networkx as nx
from .instance_repository import InstanceRepository


class FeaturesExtractor:
    def __init__(self, instance):
        self.instance = instance
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

        return features

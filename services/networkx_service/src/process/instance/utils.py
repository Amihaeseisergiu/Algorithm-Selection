import networkx as nx


class Utils:
    @staticmethod
    def construct_graph(graph_json):
        return nx.node_link_graph(graph_json, link="edges")

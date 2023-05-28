import json
import random
import networkx as nx
from pathlib import Path


def generate_graph(n_nodes, weighted=True):
    graph = nx.erdos_renyi_graph(n_nodes, p=0.2)

    if weighted:
        for (u, v, w) in graph.edges(data=True):
            w['weight'] = random.randint(0, n_nodes - 1)

    node_link_data = nx.node_link_data(graph, link="edges")

    return node_link_data


def generate_shortest_path_instance(n_nodes, weighted=True):
    instance = {
        "algorithm_type": "shortest_path",
        "parameters": {
            "source": 0,
            "target": n_nodes - 1
        },
        "graph": generate_graph(n_nodes, weighted)
    }

    save_to_file(instance, f'./output/shortest_path/shortest_path_{n_nodes}.json')


def generate_graph_coloring_instance(n_nodes, weighted=True):
    instance = {
        "algorithm_type": "coloring",
        "parameters": {
        },
        "graph": generate_graph(n_nodes, weighted)
    }

    save_to_file(instance, f'./output/coloring/coloring_{n_nodes}.json')


def save_to_file(data, path):
    Path(Path(path).parent).mkdir(parents=True, exist_ok=True)

    with open(path, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # generate_shortest_path_instance(5000)
    generate_graph_coloring_instance(10)

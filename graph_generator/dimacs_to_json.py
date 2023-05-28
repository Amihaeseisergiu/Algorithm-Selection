import os
import json
import glob
import networkx as nx
from pathlib import Path


def save_to_file(data, path):
    Path(Path(path).parent).mkdir(parents=True, exist_ok=True)

    with open(path, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def dimacs_to_graph(path):
    graph = nx.Graph()

    with open(path) as f:
        while line := f.readline():
            split_line = line.split(' ')

            if split_line[0] == 'e':
                source = int(split_line[1])
                target = int(split_line[2])

                graph.add_edge(source, target)

    return graph


def dimacs_to_json(path, algorithm_type, parameters=None):
    if parameters is None:
        parameters = {}

    graph = dimacs_to_graph(path)

    node_link_data = nx.node_link_data(graph, link="edges")

    instance = {
        "algorithm_type": algorithm_type,
        "parameters": parameters,
        "graph": node_link_data
    }

    file_name = Path(path).stem
    save_to_file(instance, f'./output/{algorithm_type}/{file_name}.json')


def all_dimacs_to_json(input_path, algorithm_type):
    for file_path in glob.glob(f"{input_path}/*.col", recursive=True):
        print(f"Converting {file_path}...")
        dimacs_to_json(file_path, algorithm_type)


def bulk_rename(path):
    for file_path in glob.glob(f"{path}/*.txt", recursive=True):
        new_name = file_path.split('.txt')[0]
        print(new_name)
        os.rename(file_path, new_name)


if __name__ == '__main__':
    all_dimacs_to_json('./input/coloring', 'coloring')

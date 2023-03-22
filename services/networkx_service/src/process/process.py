import sys

from algorithm.algorithms import Algorithms
from instance.instance_repository import InstanceRepository

if __name__ == "__main__":
    parameters = sys.argv[1:]

    instance_path = parameters[0]
    algorithm_name = parameters[1]

    instance = InstanceRepository.get_instance(instance_path)
    algorithm = Algorithms.get_mapping(instance)[algorithm_name]
    algorithm.run()

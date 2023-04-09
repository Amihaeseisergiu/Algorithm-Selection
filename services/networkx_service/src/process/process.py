import sys
import time

from algorithm.algorithms import Algorithms
from instance.instance_repository import InstanceRepository
from pubsub.selector_algorithm_publisher import SelectorAlgorithmPublisher
from pubsub.user_init_publisher import UserInitPublisher

if __name__ == "__main__":
    parameters = sys.argv[1:]

    instance_path = parameters[0]
    algorithm_name = parameters[1]
    file_id = parameters[2]
    socket_id = parameters[3]
    start_time = float(parameters[4])

    algorithmPublishers = [
        SelectorAlgorithmPublisher(file_id, algorithm_name)
    ]

    instance = InstanceRepository.get_instance(instance_path)
    algorithm = Algorithms.get_mapping(instance, algorithmPublishers)[algorithm_name]

    UserInitPublisher(socket_id, algorithm_name).send(time.time() - start_time)

    algorithm.run()

import sys
import time

from algorithm.algorithms import Algorithms
from instance.instance_repository import InstanceRepository
from pubsub.algorithms_data_publisher import AlgorithmsDataPublisher
from pubsub.user_publisher import UserPublisher
from metric.profiler import Profiler

if __name__ == "__main__":
    parameters = sys.argv[1:]

    instance_path = parameters[0]
    algorithm_name = parameters[1]
    algorithm_type = parameters[2]
    file_id = parameters[3]
    socket_id = parameters[4]
    start_time = float(parameters[5])

    profiler = Profiler(socket_id, file_id, algorithm_name, algorithm_type)
    profiler.start()

    algorithmPublishers = [
        AlgorithmsDataPublisher(file_id, algorithm_name, algorithm_type)
    ]

    instance = InstanceRepository.get_instance(instance_path)
    algorithm = Algorithms(instance, algorithmPublishers).get_algorithm(algorithm_name)

    userPublisher = UserPublisher(socket_id, algorithm_name)
    aggregatorPublisher = AlgorithmsDataPublisher(file_id, algorithm_name, algorithm_type)

    profiler.mark_initialization()
    initialization_time = time.time() - start_time
    userPublisher.send(
        {
            "event_name": "init_time",
            "payload":
                {
                    "init_time_end": initialization_time
                }
        }
    )
    aggregatorPublisher.send(
        {
            "initialization_time": initialization_time
        }
    )

    algorithm.run()
    profiler.stop()

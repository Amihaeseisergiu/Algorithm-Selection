import os
import time
from .algorithm_publisher import AlgorithmPublisher
from .consumer import Consumer


class InstanceConsumer(Consumer):
    def __init__(self):
        instances_topic = os.environ["INSTANCES_TOPIC"]
        instances_queue = os.environ["INSTANCES_QUEUE"]
        super().__init__(instances_topic, instances_queue, self.__consume_instance)

    def __consume_instance(self, data):
        print(f"[x] Processing instance {data}", flush=True)

        time.sleep(5)

        algorithm_result = str({"processed": data})

        AlgorithmPublisher().send(algorithm_result)

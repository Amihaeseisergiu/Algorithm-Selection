import os
import time
from .algorithm_publisher import AlgorithmPublisher
from .consumer import Consumer


class InstanceConsumer(Consumer):
    def __init__(self):
        instances_topic = os.environ["ALGORITHM_SELECTOR_INSTANCES_TOPIC"]
        instances_queue = os.environ["ALGORITHM_SELECTOR_INSTANCES_QUEUE"]
        super().__init__(topic=instances_topic, queue=instances_queue, exclusive=False, auto_delete=False, durable=True,
                         message_processor=self.__consume_instance)

    def __consume_instance(self, data):
        print(f"[x] Processing instance {data}", flush=True)

        time.sleep(5)

        AlgorithmPublisher().send(data)

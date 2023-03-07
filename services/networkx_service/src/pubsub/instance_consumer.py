import os
import time
import json
from .algorithm_publisher import AlgorithmPublisher
from .consumer import Consumer
from repository.instance_repository import InstanceRepository


class InstanceConsumer(Consumer):
    def __init__(self):
        instances_topic = os.environ["ALGORITHM_SELECTOR_INSTANCES_TOPIC"]
        instances_queue = os.environ["ALGORITHM_SELECTOR_INSTANCES_QUEUE"]
        super().__init__(topic=instances_topic, queue=instances_queue, exclusive=False, auto_delete=False, durable=True,
                         message_processor=self.__consume_instance)

    def __consume_instance(self, data):
        print(f"[x] Processing instance {data}", flush=True)

        data_json = json.loads(data)
        instance_data = InstanceRepository.download_instance_file(data_json["file_id"])

        print(f"[x] Instance data {instance_data}", flush=True)

        time.sleep(5)

        AlgorithmPublisher().send(data)

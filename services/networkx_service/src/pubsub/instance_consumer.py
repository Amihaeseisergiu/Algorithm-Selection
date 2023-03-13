import os
import json
from .consumer import Consumer
from algorithm.scheduler import AlgorithmScheduler
from repository.instance_repository import InstanceRepository


class InstanceConsumer(Consumer):
    def __init__(self):
        instances_topic = os.environ["ALGORITHM_SELECTOR_INSTANCES_TOPIC"]
        instances_queue = os.environ["ALGORITHM_SELECTOR_INSTANCES_QUEUE"]
        super().__init__(topic=instances_topic, queue=instances_queue, exclusive=False, auto_delete=False, durable=True,
                         message_processor=self.__consume_instance)

    def __consume_instance(self, data):
        data_json = json.loads(data)

        instance_data = InstanceRepository.download_instance_file(data_json["file_id"])
        socket_id = data_json["socket_id"]
        algorithm_type = data_json["algorithm_type"]

        print(f"[x] Instance data {instance_data}", flush=True)

        scheduler = AlgorithmScheduler(socket_id, algorithm_type)
        scheduler.schedule(data)

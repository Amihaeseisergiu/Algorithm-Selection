import os
import json
from threading import Thread
from .consumer import Consumer
from algorithm.scheduler import AlgorithmScheduler
from repository.instance_repository import InstanceRepository


class InstanceConsumer(Consumer):
    def __init__(self):
        instances_topic = os.environ["INSTANCES_TOPIC"]
        instances_queue = os.environ["INSTANCES_QUEUE"]
        super().__init__(topic=instances_topic, exchange_type='fanout', queue=instances_queue, exclusive=False,
                         auto_delete=False, durable=True, message_processor=self.__consume)

    def __consume_instance(self, data):
        data_json = json.loads(data)

        instance_data = InstanceRepository.download_instance_file(data_json["file_id"])
        socket_id = data_json["socket_id"]
        algorithm_type = data_json["algorithm_type"]

        print(f"[x] Instance data {instance_data}, socket_id {socket_id}", flush=True)

        scheduler = AlgorithmScheduler(socket_id, algorithm_type)
        scheduler.schedule(data)

    def __consume(self, data):
        thread = Thread(target=self.__consume_instance, args=(data,))
        thread.start()

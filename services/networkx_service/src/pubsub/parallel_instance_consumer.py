import os
import json
from threading import Thread
from executor.parallel_executor import ParallelExecutor
from .consumer import Consumer
from repository.instance_repository import InstanceRepository


class ParallelInstanceConsumer(Consumer):
    def __init__(self):
        instances_topic = os.environ["INSTANCES_TOPIC"]
        instances_queue = os.environ["INSTANCES_PARALLEL_QUEUE"]
        instances_key = os.environ["INSTANCES_PARALLEL_KEY"]
        super().__init__(topic=instances_topic, exchange_type='topic', queue=instances_queue,
                         routing_key=instances_key, exclusive=False, auto_delete=False, durable=True,
                         message_processor=self.__consume)

    def __consume_instance(self, data):
        data_json = json.loads(data)
        socket_id = data_json["socket_id"]
        file_id = data_json["file_id"]
        file_name = data_json["file_name"]
        web_service_id = data_json["web_service_id"]

        algorithm_type, instance_path = InstanceRepository.download_instance_file(file_id, web_service_id)
        ParallelExecutor(socket_id, file_id, file_name, algorithm_type, instance_path).execute()

    def __consume(self, data):
        thread = Thread(target=self.__consume_instance, args=(data,))
        thread.start()

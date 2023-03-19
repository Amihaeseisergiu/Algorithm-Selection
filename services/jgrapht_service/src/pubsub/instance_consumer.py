import os
import json
from threading import Thread
from scheduler.scheduler_provider import SchedulerProvider
from .consumer import Consumer
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
        instance_json = json.loads(instance_data)

        algorithm_type = instance_json["algorithm_type"]
        socket_id = data_json["socket_id"]

        scheduler = SchedulerProvider(socket_id).get(algorithm_type)
        scheduler.schedule(instance_json)

    def __consume(self, data):
        thread = Thread(target=self.__consume_instance, args=(data,))
        thread.start()
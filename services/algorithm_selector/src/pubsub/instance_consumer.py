import os
from .consumer import Consumer


class InstanceConsumer(Consumer):
    def __init__(self):
        instances_topic = os.environ["INSTANCES_TOPIC"]
        instances_queue = os.environ["INSTANCES_QUEUE"]
        super().__init__(topic=instances_topic, exchange_type='fanout', queue=instances_queue, exclusive=False,
                         auto_delete=False, durable=True, message_processor=self.__consume_instance)

    def __consume_instance(self, data):
        print(f"[x] Received web service instance {data}", flush=True)

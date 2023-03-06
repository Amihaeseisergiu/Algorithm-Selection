import os
from .consumer import Consumer
from .instance_publisher import InstancePublisher


class InstanceConsumer(Consumer):
    def __init__(self):
        instances_topic = os.environ["WEB_SERVICE_INSTANCES_TOPIC"]
        instances_queue = os.environ["WEB_SERVICE_INSTANCES_QUEUE"]
        super().__init__(topic=instances_topic, queue=instances_queue, exclusive=False, auto_delete=False,
                         durable=True, message_processor=self.__consume_instance)

    def __consume_instance(self, data):
        print(f"[x] Received web service instance {data}", flush=True)

        InstancePublisher().send(data)

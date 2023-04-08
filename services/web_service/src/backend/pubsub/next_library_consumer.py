import os
import json
from .consumer import Consumer
from .instance_publisher import InstancePublisher


class NextLibraryConsumer(Consumer):
    def __init__(self, socket_id):
        next_library_topic = os.environ["NEXT_LIBRARY_TOPIC"]
        routing_key = f"{socket_id}_next_library"
        super().__init__(topic=next_library_topic, exchange_type='direct', queue=routing_key, routing_key=routing_key,
                         auto_delete=True, durable=False, exclusive=True, message_processor=self.__next_library,
                         socketio=None)

    def __next_library(self, data):
        data_json = json.loads(data)

        available_libraries = os.environ["SEQUENTIAL_LIBRARY_NAMES"].split(',')
        next_library = int(data_json['current_library']) + 1
        data_json['current_library'] = next_library

        if next_library < len(available_libraries):
            next_library_name = available_libraries[next_library]
            routing_key = f"{os.environ['INSTANCES_SEQUENTIAL_KEY_PREFIX']}.{next_library_name}"

            InstancePublisher(routing_key).send(json.dumps(data_json))

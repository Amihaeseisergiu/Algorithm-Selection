import os
import json
from .consumer import Consumer


class AlgorithmConsumer(Consumer):
    def __init__(self, socketio, routing_key):
        algorithms_topic = os.environ["ALGORITHMS_TOPIC"]
        super().__init__(topic=algorithms_topic, exchange_type='direct', queue=routing_key, routing_key=routing_key,
                         auto_delete=True, durable=False, exclusive=True, message_processor=self.__consume_algorithm,
                         socketio=socketio)

    def __consume_algorithm(self, data):
        data_json = json.loads(data)
        socket_id = data_json["header"]["socket_id"]
        event_name = data_json["header"]["event_name"]

        self.socketio.emit(event_name, data_json, to=socket_id)

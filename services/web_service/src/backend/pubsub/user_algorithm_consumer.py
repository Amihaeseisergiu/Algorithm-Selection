import os
import json
from .consumer import Consumer


class UserAlgorithmConsumer(Consumer):
    def __init__(self, socketio, socket_id):
        user_algorithm_topic = os.environ["USER_ALGORITHM_TOPIC"]
        routing_key = f"{socket_id}_user_algorithm"
        super().__init__(topic=user_algorithm_topic, exchange_type='direct', queue=routing_key, routing_key=routing_key,
                         auto_delete=True, durable=False, exclusive=True, message_processor=self.__consume_algorithm,
                         socketio=socketio)

    def __consume_algorithm(self, data):
        data_json = json.loads(data)
        socket_id = data_json["header"]["socket_id"]
        event_name = data_json["header"]["event_name"]

        self.socketio.emit(event_name, data_json, to=socket_id)

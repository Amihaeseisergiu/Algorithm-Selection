import os
import json
from .consumer import Consumer


class AlgorithmConsumer(Consumer):
    def __init__(self, socketio):
        algorithms_topic = os.environ["ALGORITHM_SELECTOR_ALGORITHM_RESPONSES_TOPIC"]
        super().__init__(topic=algorithms_topic, queue="", auto_delete=True, durable=False, exclusive=True,
                         message_processor=self.__consume_algorithm, socketio=socketio)

    def __consume_algorithm(self, data):
        print(f"[x] Received algorithm response {data}", flush=True)

        data_json = json.loads(data)
        socket_id = data_json["header"]["socket_id"]
        event_name = data_json["header"]["event_name"]

        self.socketio.emit(event_name, data_json, to=socket_id)

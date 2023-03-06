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

        json_data = json.loads(data)

        self.socketio.emit("receive_algorithm_response", json_data, to=json_data["socket_id"])

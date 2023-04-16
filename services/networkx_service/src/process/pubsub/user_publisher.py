import os
import json
from .publisher import Publisher
from network.envelope import Envelope


class UserPublisher(Publisher):
    def __init__(self, socket_id, algorithm_name, algorithm_type):
        user_metrics_topic = os.environ["USER_METRICS_TOPIC"]
        routing_key = f"{socket_id}_user_metric"
        super().__init__(user_metrics_topic, routing_key, 'direct')

        self.socket_id = socket_id
        self.algorithm_name = algorithm_name
        self.envelope = Envelope.send_user_data(self.socket_id, self.algorithm_name)

    def send(self, data):
        event_name = data['event_name']
        payload = data['payload']

        self.envelope['header']['event_name'] = event_name
        self.envelope['payload'] = payload

        super().send(json.dumps(self.envelope), 0)

import os
import json
from .publisher import Publisher
from network.envelope import Envelope


class UserInitPublisher(Publisher):
    def __init__(self, socket_id, algorithm_name):
        user_metrics_topic = os.environ["USER_METRICS_TOPIC"]
        routing_key = f"{socket_id}_user_metric"
        super().__init__(user_metrics_topic, routing_key, 'direct')

        self.socket_id = socket_id
        self.algorithm_name = algorithm_name

    def send(self, time):
        envelope = Envelope.send_user_init_time(self.socket_id, self.algorithm_name, time)
        super().send(json.dumps(envelope), 0)

import os
from .publisher import Publisher


class UserAlgorithmPublisher(Publisher):
    def __init__(self, socket_id):
        user_metrics_topic = os.environ["USER_ALGORITHM_TOPIC"]
        routing_key = f"{socket_id}_user_algorithm"
        super().__init__(user_metrics_topic, routing_key, 'direct')

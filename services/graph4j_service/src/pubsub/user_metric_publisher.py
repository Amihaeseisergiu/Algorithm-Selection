import os
from .publisher import Publisher


class UserMetricPublisher(Publisher):
    def __init__(self, routing_key):
        user_metrics_topic = os.environ["USER_METRICS_TOPIC"]
        super().__init__(user_metrics_topic, routing_key, 'direct')

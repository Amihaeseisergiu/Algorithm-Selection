import os
from .publisher import Publisher


class AlgorithmPublisher(Publisher):
    def __init__(self, routing_key):
        algorithms_topic = os.environ["ALGORITHMS_TOPIC"]
        super().__init__(algorithms_topic, routing_key, 'direct')

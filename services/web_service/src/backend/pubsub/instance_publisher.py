import os
from .publisher import Publisher


class InstancePublisher(Publisher):
    def __init__(self, routing_key):
        topic = os.environ["INSTANCES_TOPIC"]
        super().__init__(topic, routing_key, 'topic')

import os
from .publisher import Publisher


class InstancePublisher(Publisher):
    def __init__(self):
        instances_topic = os.environ["ALGORITHM_SELECTOR_INSTANCES_TOPIC"]
        super().__init__(instances_topic)
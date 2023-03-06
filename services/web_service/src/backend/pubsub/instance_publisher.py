import os
from .publisher import Publisher


class InstancePublisher(Publisher):
    def __init__(self):
        instances_topic = os.environ["WEB_SERVICE_INSTANCES_TOPIC"]
        super().__init__(instances_topic)

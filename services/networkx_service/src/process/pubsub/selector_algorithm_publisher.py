import os
from .publisher import Publisher


class SelectorAlgorithmPublisher(Publisher):
    def __init__(self):
        selector_algorithms_topic = os.environ["SELECTOR_ALGORITHMS_TOPIC"]
        super().__init__(selector_algorithms_topic, '', 'fanout')

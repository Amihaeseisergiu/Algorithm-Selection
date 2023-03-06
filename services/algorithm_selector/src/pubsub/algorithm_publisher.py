import os
from .publisher import Publisher


class AlgorithmPublisher(Publisher):
    def __init__(self):
        algorithms_topic = os.environ["ALGORITHM_SELECTOR_ALGORITHM_RESPONSES_TOPIC"]
        super().__init__(algorithms_topic)

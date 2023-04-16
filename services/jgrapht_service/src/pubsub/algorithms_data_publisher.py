import os
from .publisher import Publisher


class AlgorithmsDataPublisher(Publisher):
    def __init__(self):
        data_aggregator_topic = os.environ["DATA_AGGREGATOR_TOPIC"]
        algorithms_data_key = os.environ["ALGORITHMS_DATA_KEY"]
        super().__init__(data_aggregator_topic, algorithms_data_key, 'topic')

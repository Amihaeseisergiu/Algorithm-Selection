import os
from .publisher import Publisher


class DatasetEntryPublisher(Publisher):
    def __init__(self):
        dataset_entry_topic = os.environ["DATASET_ENTRY_TOPIC"]
        super().__init__(dataset_entry_topic, "", 'fanout')

import os
import json
from .consumer import Consumer


class DatasetEntryConsumer(Consumer):
    def __init__(self):
        dataset_entry_topic = os.environ["DATASET_ENTRY_TOPIC"]
        dataset_entry_queue = os.environ["DATASET_ENTRY_QUEUE"]
        super().__init__(topic=dataset_entry_topic, exchange_type='fanout', queue=dataset_entry_queue,
                         routing_key="", exclusive=False, auto_delete=False, durable=True,
                         message_processor=self.__consume_dataset_entry)

    def __consume_dataset_entry(self, data):
        print(f"[X] Received dataset entry {data}", flush=True)
        data_json = json.loads(data)

import os
import json
from .consumer import Consumer
from repository.database import Database
from repository.schema import Schema


class DatasetEntryConsumer(Consumer):
    def __init__(self):
        dataset_entry_topic = os.environ["DATASET_ENTRY_TOPIC"]
        dataset_entry_queue = os.environ["DATASET_ENTRY_QUEUE"]
        super().__init__(topic=dataset_entry_topic, exchange_type='fanout', queue=dataset_entry_queue,
                         routing_key="", exclusive=False, auto_delete=False, durable=True,
                         message_processor=self.__consume_dataset_entry)

    def __consume_dataset_entry(self, data):
        data_json = json.loads(data)

        schema_class = Schema.create_algorithm_type_schema(data_json['algorithm_type'])

        entry = {
            "algorithm": data_json["algorithm_name"],
            "library": data_json["library_name"]
        }

        Database.client.data_object.create(
            entry,
            schema_class,
            vector=data_json['features']
        )

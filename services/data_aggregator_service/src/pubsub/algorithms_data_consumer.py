import os
import json
import pymongo
from repository.database import Database
from .consumer import Consumer


class AlgorithmsDataConsumer(Consumer):
    def __init__(self):
        data_aggregator_topic = os.environ["DATA_AGGREGATOR_TOPIC"]
        algorithms_data_queue = os.environ["ALGORITHMS_DATA_QUEUE"]
        algorithms_data_key = os.environ["ALGORITHMS_DATA_KEY"]
        super().__init__(topic=data_aggregator_topic, exchange_type='topic', queue=algorithms_data_queue,
                         routing_key=algorithms_data_key, exclusive=False,
                         auto_delete=False, durable=True, message_processor=self.__consume_algorithms_data)

    def __consume_algorithms_data(self, data):
        print(f"[X] Received algorithm data {data}")
        data_json = json.loads(data)
        features = data_json["header"] | data_json["payload"]

        file_id = features["file_id"]
        library_name = features["library_name"]
        algorithm_name = features["algorithm_name"]

        algorithms_aggregations = Database.get("data")["algorithms-data"]
        algorithms_aggregations.create_index(
            keys=[
                ("file_id", pymongo.ASCENDING),
                ("library_name", pymongo.ASCENDING),
                ("algorithm_name", pymongo.ASCENDING)
            ],
            unique=True
        )

        algorithms_aggregations.update_one(
            filter={
                "file_id": file_id,
                "library_name": library_name,
                "algorithm_name": algorithm_name
            },
            update={"$set": features},
            upsert=True
        )

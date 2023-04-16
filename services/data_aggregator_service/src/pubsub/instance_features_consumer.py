import os
import json
import pymongo
from repository.database import Database
from .consumer import Consumer


class InstanceFeaturesConsumer(Consumer):
    def __init__(self):
        data_aggregator_topic = os.environ["DATA_AGGREGATOR_TOPIC"]
        instance_features_queue = os.environ["INSTANCE_FEATURES_QUEUE"]
        instance_features_key = os.environ["INSTANCE_FEATURES_KEY"]
        super().__init__(topic=data_aggregator_topic, exchange_type='topic', queue=instance_features_queue,
                         routing_key=instance_features_key, exclusive=False,
                         auto_delete=False, durable=True, message_processor=self.__consume_instance_features)

    def __consume_instance_features(self, data):
        print(f"[X] Received instance features: {data}", flush=True)
        data_json = json.loads(data)
        features = data_json["header"] | data_json["payload"]

        file_id = features["file_id"]
        library_name = features["library_name"]

        algorithms_aggregations = Database.get("data")["algorithms-data"]
        algorithms_aggregations.create_index(
            keys=[
                ("file_id", pymongo.ASCENDING),
                ("library_name", pymongo.ASCENDING),
                ("algorithm_name", pymongo.ASCENDING)
            ],
            unique=True
        )

        algorithms_aggregations.update_many(
            filter={
                "file_id": file_id,
                "library_name": library_name
            },
            update={"$set": features},
            upsert=True
        )
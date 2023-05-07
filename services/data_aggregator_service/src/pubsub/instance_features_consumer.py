import os
import json
import pymongo
from repository.database import Database
from pubsub.dataset_entry_publisher import DatasetEntryPublisher
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
        data_json = json.loads(data)
        features = data_json["header"] | data_json["payload"]

        file_id = features["file_id"]
        library_name = features["library_name"]

        algorithms_aggregations_collection = Database.get("data")["algorithms-data"]
        algorithms_aggregations_collection.create_index(
            keys=[
                ("file_id", pymongo.ASCENDING),
                ("library_name", pymongo.ASCENDING),
                ("algorithm_name", pymongo.ASCENDING)
            ],
            unique=True
        )

        algorithms_aggregations_collection.update_many(
            filter={
                "file_id": file_id,
                "library_name": library_name
            },
            update=[
                {
                    "$set": features
                },
                {
                    "$set": {
                        "algorithm_execution_time": {
                            "$subtract": ["$total_time", "$initialization_time"]
                        },
                        "score": {
                            "$add": [
                                {
                                    "$multiply": [
                                        0.99,
                                        {
                                            "$subtract": [
                                                "$total_time",
                                                "$initialization_time"
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "$multiply": [
                                        0.01,
                                        {
                                            "$add": [
                                                "$avg_memory",
                                                "$avg_cpu"
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                }
            ],
            upsert=True
        )

        libraries_winners_collection = Database.get("data")["libraries-winners"]
        libraries_winners_collection.create_index(
            keys=[
                ("file_id", pymongo.ASCENDING),
                ("library_name", pymongo.ASCENDING)
            ],
            unique=True
        )

        library_algorithms = list(algorithms_aggregations_collection.aggregate(
            [
                {
                    "$match": {
                        "file_id": file_id,
                        "library_name": library_name
                    }
                }
            ]
        ))

        library_winner = sorted(library_algorithms,
                                key=lambda e: (e['result'], e['heuristic_score'], e['score']))[0]

        libraries_winners_collection.update_one(
            filter={
                "file_id": file_id,
                "library_name": library_name
            },
            update={
                "$set": library_winner
            },
            upsert=True
        )

        n_libraries = len(os.environ["LIBRARY_NAMES"].split(','))
        libraries_algorithms = list(libraries_winners_collection.aggregate(
            [
                {
                    "$match": {
                        "file_id": file_id
                    }
                },
                {
                    "$project": {
                        "_id": 0
                    }
                }
            ]
        ))

        if len(libraries_algorithms) == n_libraries:
            global_winner = sorted(libraries_algorithms,
                                   key=lambda e: (e['result'], e['heuristic_score'], e['score']))[0]

            dataset_collection = Database.get("data")["dataset"]
            dataset_collection.create_index(
                keys=[
                    ("file_id", pymongo.ASCENDING),
                    ("library_name", pymongo.ASCENDING),
                    ("algorithm_name", pymongo.ASCENDING)
                ],
                unique=True
            )
            dataset_collection.update_one(
                filter={
                    "file_id": file_id
                },
                update={
                    "$set": global_winner
                },
                upsert=True
            )

            DatasetEntryPublisher().send(json.dumps(global_winner))

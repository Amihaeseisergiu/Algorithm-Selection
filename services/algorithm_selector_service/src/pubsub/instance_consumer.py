import os
import json
from collections import Counter
from .consumer import Consumer
from .user_algorithm_publisher import UserAlgorithmPublisher
from repository.features_extractor import FeaturesExtractor
from repository.database import Database
from repository.schema import Schema
from repository.instance_repository import InstanceRepository
from network.envelope import Envelope


class InstanceConsumer(Consumer):
    def __init__(self):
        instances_topic = os.environ["INSTANCES_TOPIC"]
        instances_queue = os.environ["INSTANCES_QUEUE"]
        instances_key = os.environ["INSTANCES_KEY"]
        super().__init__(topic=instances_topic, exchange_type='topic', queue=instances_queue,
                         routing_key=instances_key, exclusive=False, auto_delete=False, durable=True,
                         message_processor=self.__consume_instance)

    def __consume_instance(self, data):
        try:
            data_json = json.loads(data)

            socket_id = data_json["socket_id"]
            file_id = data_json["file_id"]
            web_service_id = data_json["web_service_id"]

            instance = InstanceRepository.get_instance_file(file_id, web_service_id)
            algorithm_type = instance['algorithm_type']
            schema_class = Schema.create_algorithm_type_schema(algorithm_type)
            features = FeaturesExtractor(instance).extract()

            results = (
                Database.client.query
                .get(schema_class, ["algorithm", "library"])
                .with_near_vector({
                    "vector": features,
                    "certainty": 0.7
                })
                .with_limit(int(os.environ["MAJORITY_VOTING_DATAPOINTS"]))
                .do()
            )['data']['Get'][schema_class]

            user_envelope = Envelope.create_end_user_envelope(socket_id, "selected_data")

            if results:
                print(f"[X] Closest points: {results}", flush=True)

                results_libraries = Counter()
                results_algorithms = Counter()

                for result in results:
                    results_libraries[result['library']] += 1
                    results_algorithms[result['algorithm']] += 1

                user_envelope['payload'] = {
                    'library': results_libraries.most_common(1)[0][0],
                    'algorithm': results_algorithms.most_common(1)[0][0]
                }
            else:
                user_envelope['header']['error'] = 'Unavailable dataset'

            UserAlgorithmPublisher(socket_id).send(json.dumps(user_envelope))
        except Exception as e:
            print(e, flush=True)
            raise e

import json
from network.envelope import Envelope
from algorithm.algorithms import Algorithms
from repository.features_extractor import FeaturesExtractor
from pubsub.user_metric_publisher import UserMetricPublisher


class ParallelExecutor:
    def __init__(self, socket_id, file_id, file_name, algorithm_type, instance_path):
        self.socket_id = socket_id
        self.file_id = file_id
        self.file_name = file_name
        self.instance_path = instance_path
        self.algorithm_type = algorithm_type
        self.algorithms = Algorithms(socket_id, file_id).get(algorithm_type)

    def __library_end(self):
        user_envelope = Envelope.create_end_user_envelope(socket_id=self.socket_id, event_name="library_end")
        UserMetricPublisher(self.socket_id).send(json.dumps(user_envelope))

        FeaturesExtractor(file_id=self.file_id, file_name=self.file_name, algorithm_type=self.algorithm_type).extract()

    def execute(self):
        threads = []

        for algorithm in self.algorithms:
            thread = algorithm.create(self.instance_path)
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self.__library_end()

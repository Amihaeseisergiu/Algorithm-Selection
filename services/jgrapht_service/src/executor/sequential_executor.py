import json
from network.envelope import Envelope
from algorithm.algorithms import Algorithms
from repository.features_extractor import FeaturesExtractor
from pubsub.user_metric_publisher import UserMetricPublisher
from pubsub.next_library_publisher import NextLibraryPublisher


class SequentialExecutor:
    def __init__(self, socket_id, file_id, algorithm_type, instance_path, bounce_instance_data):
        self.socket_id = socket_id
        self.file_id = file_id
        self.instance_path = instance_path
        self.algorithm_type = algorithm_type
        self.bounce_instance_data = bounce_instance_data
        self.algorithms = Algorithms(socket_id, file_id).get(algorithm_type)

    def __library_end(self):
        user_envelope = Envelope.create_end_user_envelope(socket_id=self.socket_id, event_name="library_end")
        UserMetricPublisher(self.socket_id).send(json.dumps(user_envelope))
        NextLibraryPublisher(self.socket_id).send(json.dumps(self.bounce_instance_data))

        FeaturesExtractor(file_id=self.file_id, algorithm_type=self.algorithm_type).extract()

    def execute(self):
        for algorithm in self.algorithms:
            envelope = Envelope.create_end_user_envelope(socket_id=self.socket_id, event_name="schedule")
            envelope["header"]["algorithm_name"] = algorithm.algorithm_name
            UserMetricPublisher(self.socket_id).send(json.dumps(envelope))

        for algorithm in self.algorithms:
            thread = algorithm.create(self.instance_path)
            thread.start()
            thread.join()

        self.__library_end()

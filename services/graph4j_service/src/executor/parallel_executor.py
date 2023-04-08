import json
from network.envelope import Envelope
from pubsub.user_metric_publisher import UserMetricPublisher
from algorithm.algorithms import Algorithms


class ParallelExecutor:
    def __init__(self, socket_id, file_id, algorithm_type, instance_path):
        self.socket_id = socket_id
        self.file_id = file_id
        self.instance_path = instance_path
        self.algorithms = Algorithms(socket_id, file_id).get(algorithm_type)

    def __library_end(self):
        envelope = Envelope.create_end_user_envelope(socket_id=self.socket_id, event_name="library_end")
        UserMetricPublisher(self.socket_id).send(json.dumps(envelope))

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

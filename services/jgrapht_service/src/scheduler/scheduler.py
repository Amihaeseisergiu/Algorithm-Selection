import json
from network.envelope import Envelope
from pubsub.algorithm_publisher import AlgorithmPublisher


class AlgorithmScheduler:
    def __init__(self, socket_id, algorithms):
        self.socket_id = socket_id
        self.algorithms = algorithms

    def __library_end(self):
        envelope = Envelope.create_end_user_envelope(socket_id=self.socket_id, event_name="library_end")
        AlgorithmPublisher(self.socket_id).send(json.dumps(envelope))

    def schedule(self, instance_path):
        threads = []

        for algorithm in self.algorithms:
            thread = algorithm.create(instance_path)
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        self.__library_end()

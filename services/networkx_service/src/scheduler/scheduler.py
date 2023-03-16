import json
from network.envelope import Envelope
from pubsub.algorithm_publisher import AlgorithmPublisher


class AlgorithmScheduler:
    def __init__(self, socket_id, algorithms):
        self.socket_id = socket_id
        self.algorithms = algorithms

    def __emit_library_state(self, state):
        envelope = Envelope.create_end_user_envelope(socket_id=self.socket_id, event_name="library_emit")
        envelope["payload"] = {
            "emit_state": state,
        }

        AlgorithmPublisher(self.socket_id).send(json.dumps(envelope))

    def schedule(self, data):
        started_threads = []

        for algorithm in self.algorithms:
            thread = algorithm.run(data)
            started_threads.append(thread)

        for thread in started_threads:
            thread.join()

        self.__emit_library_state("end")

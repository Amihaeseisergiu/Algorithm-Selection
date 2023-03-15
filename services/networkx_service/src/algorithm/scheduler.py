import json
from algorithm.runner import AlgorithmRunner
from network.envelope import Envelope
from pubsub.algorithm_publisher import AlgorithmPublisher


class AlgorithmScheduler:
    def __init__(self, socket_id, algorithm_type):
        self.socket_id = socket_id
        self.algorithm_type = algorithm_type

    def __emit_library_state(self, state):
        envelope = Envelope.create_end_user_envelope(socket_id=self.socket_id, event_name="library_emit")
        envelope["payload"] = {
            "emit_state": state,
        }

        AlgorithmPublisher(self.socket_id).send(json.dumps(envelope))

    def schedule(self, data):
        algorithm1 = AlgorithmRunner(self.socket_id, "Dijkstra").run(data)
        algorithm2 = AlgorithmRunner(self.socket_id, "A*").run(data)

        algorithm1.join()
        algorithm2.join()

        self.__emit_library_state("end")

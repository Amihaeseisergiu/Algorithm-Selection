import json
import time
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

        AlgorithmPublisher().send(json.dumps(envelope))

    def schedule(self, data):
        runner = AlgorithmRunner(self.socket_id, "Dijkstra")
        runner.run(data)

        time.sleep(2)

        runner = AlgorithmRunner(self.socket_id, "A*")
        runner.run(data)

        self.__emit_library_state("end")

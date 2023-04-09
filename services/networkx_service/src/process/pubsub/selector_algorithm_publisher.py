import os
import json
from .publisher import Publisher
from network.envelope import Envelope


class SelectorAlgorithmPublisher(Publisher):
    def __init__(self, file_id, algorithm_name):
        super().__init__(os.environ["SELECTOR_ALGORITHMS_TOPIC"], '', 'fanout')
        self.file_id = file_id
        self.algorithm_name = algorithm_name

    def send(self, result):
        envelope = Envelope.send_selector_algorithm_result(self.file_id, self.algorithm_name, result)
        super().send(json.dumps(envelope), 0)

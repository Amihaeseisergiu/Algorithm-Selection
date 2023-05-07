import os
import json
from .publisher import Publisher
from network.envelope import Envelope


class AlgorithmsDataPublisher(Publisher):
    def __init__(self, file_id, algorithm_name, algorithm_type):
        super().__init__(os.environ["DATA_AGGREGATOR_TOPIC"], os.environ['ALGORITHMS_DATA_KEY'], 'topic')
        self.file_id = file_id
        self.algorithm_name = algorithm_name
        self.algorithm_type = algorithm_type
        self.envelope = Envelope.send_algorithm_data(self.file_id, self.algorithm_name, self.algorithm_type)

    def send(self, data):
        self.envelope['payload'] = data

        return super().send(json.dumps(self.envelope))

import logging
from .consumer import Consumer


class AlgorithmConsumer(Consumer):
    def __init__(self, topic):
        super().__init__(topic, self._consume_algorithm)

        self.number_of_calls = 0

    def _consume_algorithm(self, channel, method, properties, body):
        self.number_of_calls += 1
        print(f"[x] [{self.number_of_calls}] Received algorithm response {body}", flush=True)

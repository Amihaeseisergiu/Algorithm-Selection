import os
import logging
from .consumer import Consumer
from .publisher import Publisher


class InstanceConsumer(Consumer):
    def __init__(self, topic):
        super().__init__(topic, self._consume_instance)
        self.number_of_calls = 0

    def _consume_instance(self, channel, method, properties, body):
        self.number_of_calls += 1
        print(f"[x] [{self.number_of_calls}] Received instance to process {body}", flush=True)

        algorithm_result = str({"processed": body})

        algorithms_topic = os.environ["ALGORITHMS_TOPIC"]
        Publisher(algorithms_topic).send(algorithm_result)

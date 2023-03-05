import os
from .consumer import Consumer


class AlgorithmConsumer(Consumer):
    def __init__(self):
        algorithms_topic = os.environ["ALGORITHMS_TOPIC"]
        algorithms_queue = os.environ["ALGORITHMS_QUEUE"]
        super().__init__(algorithms_topic, algorithms_queue, self.__consume_algorithm)

    def __consume_algorithm(self, data):
        print(f"[x] Received algorithm response {data}", flush=True)

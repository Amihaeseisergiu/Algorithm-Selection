import os
from .consumer import Consumer


class SelectorAlgorithmConsumer(Consumer):
    def __init__(self):
        selector_algorithms_topic = os.environ["SELECTOR_ALGORITHMS_TOPIC"]
        super().__init__(topic=selector_algorithms_topic, exchange_type='fanout', queue='', exclusive=True,
                         auto_delete=False, durable=True, message_processor=self.__consume_algorithm)

    def __consume_algorithm(self, data):
        print(f"[x] Received algorithm response {data}", flush=True)

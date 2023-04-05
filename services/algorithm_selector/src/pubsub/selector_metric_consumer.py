import os
from .consumer import Consumer


class SelectorMetricConsumer(Consumer):
    def __init__(self):
        selector_metrics_topic = os.environ["SELECTOR_METRICS_TOPIC"]
        super().__init__(topic=selector_metrics_topic, exchange_type='fanout', queue='', exclusive=True,
                         auto_delete=False, durable=True, message_processor=self.__consume_metric)

    def __consume_metric(self, data):
        print(f"[x] Received metric response {data}", flush=True)

import os
from .publisher import Publisher


class SelectorMetricPublisher(Publisher):
    def __init__(self):
        selector_metrics_topic = os.environ["SELECTOR_METRICS_TOPIC"]
        super().__init__(selector_metrics_topic, '', 'fanout')

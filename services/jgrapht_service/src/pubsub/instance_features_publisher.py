import os
from .publisher import Publisher


class InstanceFeaturesPublisher(Publisher):
    def __init__(self):
        data_aggregator_topic = os.environ["DATA_AGGREGATOR_TOPIC"]
        instance_features_key = os.environ["INSTANCE_FEATURES_KEY"]
        super().__init__(data_aggregator_topic, instance_features_key, 'topic')

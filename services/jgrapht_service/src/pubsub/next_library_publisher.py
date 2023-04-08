import os
from .publisher import Publisher


class NextLibraryPublisher(Publisher):
    def __init__(self, socket_id):
        user_metrics_topic = os.environ["NEXT_LIBRARY_TOPIC"]
        routing_key = f"{socket_id}_next_library"
        super().__init__(user_metrics_topic, routing_key, 'direct')

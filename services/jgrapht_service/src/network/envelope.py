
class Envelope:
    @staticmethod
    def create_end_user_envelope(socket_id, event_name):
        return {
            "header": {
                "socket_id": socket_id,
                "event_name": event_name,
                "library_name": "JGraphT"
            },
            "payload": {}
        }

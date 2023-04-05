import os


class Envelope:
    @staticmethod
    def create_end_user_envelope(socket_id, event_name):
        library_name = os.environ["LIBRARY_NAME"]

        return {
            "header": {
                "socket_id": socket_id,
                "event_name": event_name,
                "library_name": library_name
            },
            "payload": {}
        }

    @staticmethod
    def create_selector_envelope(file_id, algorithm_name):
        library_name = os.environ["LIBRARY_NAME"]

        return {
            "header": {
                "file_id": file_id,
                "algorithm_name": algorithm_name,
                "library_name": library_name
            },
            "payload": {}
        }
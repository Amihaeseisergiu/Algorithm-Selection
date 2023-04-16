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
    def create_algorithm_data_envelope(file_id, algorithm_name, algorithm_type):
        library_name = os.environ["LIBRARY_NAME"]

        return {
            "header": {
                "file_id": file_id,
                "algorithm_name": algorithm_name,
                "algorithm_type": algorithm_type,
                "library_name": library_name
            },
            "payload": {}
        }

    @staticmethod
    def create_instance_features_envelope(file_id, algorithm_type):
        library_name = os.environ["LIBRARY_NAME"]

        return {
            "header": {
                "file_id": file_id,
                "algorithm_type": algorithm_type,
                "library_name": library_name
            },
            "payload": {}
        }
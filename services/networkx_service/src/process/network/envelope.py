import os


class Envelope:
    @staticmethod
    def send_algorithm_data(file_id, algorithm_name, algorithm_type):
        library_name = os.environ["LIBRARY_NAME"]

        return {
            "header": {
                "file_id": file_id,
                "algorithm_name": algorithm_name,
                "algorithm_type": algorithm_type,
                "library_name": library_name
            }
        }

    @staticmethod
    def send_user_data(socket_id, algorithm_name):
        library_name = os.environ["LIBRARY_NAME"]

        return {
            "header": {
                "socket_id": socket_id,
                "library_name": library_name,
                "algorithm_name": algorithm_name,
            }
        }
import os


class Envelope:
    @staticmethod
    def send_selector_algorithm_result(file_id, algorithm_name, result):
        library_name = os.environ["LIBRARY_NAME"]

        return {
            "header": {
                "file_id": file_id,
                "algorithm_name": algorithm_name,
                "library_name": library_name
            },
            "payload": {
                "result": result
            }
        }

    @staticmethod
    def send_user_init_time(socket_id, algorithm_name, time):
        library_name = os.environ["LIBRARY_NAME"]

        return {
            "header": {
                "socket_id": socket_id,
                "event_name": "init_time",
                "library_name": library_name,
                "algorithm_name": algorithm_name,
            },
            "payload": {
                "init_time_end": time
            }
        }
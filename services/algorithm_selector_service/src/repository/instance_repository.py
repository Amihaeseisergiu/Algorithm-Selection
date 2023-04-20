import json
import requests


class InstanceRepository:
    @staticmethod
    def get_instance_file(file_id, web_service_id):
        instance_data = requests.get(f"http://{web_service_id}:5000/download/{file_id}")
        instance_json = json.loads(instance_data.json())

        return instance_json

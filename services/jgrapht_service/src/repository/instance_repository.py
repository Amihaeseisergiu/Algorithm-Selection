import os
import json
import shutil
import requests


class InstanceRepository:
    @staticmethod
    def download_instance_file(file_id):
        web_service_name = os.environ['WEB_SERVICE_NAME']
        instance_data = requests.get(f"http://{web_service_name}:5000/download/{file_id}")
        instance_json = json.loads(instance_data.json())

        directory_path = f"/files"
        file_path = f'{directory_path}/{file_id}'

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        with open(file_path, "wb") as f:
            f.write(instance_data.content)

        return instance_json['algorithm_type'], file_path

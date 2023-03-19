import os

import requests


class InstanceRepository:
    @staticmethod
    def download_instance_file(file_id):
        web_service_name = os.environ['WEB_SERVICE_NAME']
        instance_data = requests.get(f"http://{web_service_name}:5000/download/{file_id}")

        return instance_data.json()

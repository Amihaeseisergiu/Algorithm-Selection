import os
from flask_restful import Resource


class Download(Resource):
    def get(self, file_id):
        file_path = f"../files/{file_id}"

        if not os.path.isfile(file_path):
            return "Not Found", 404

        with open(f"../files/{file_id}") as f:
            file_content = f.read()

        return file_content

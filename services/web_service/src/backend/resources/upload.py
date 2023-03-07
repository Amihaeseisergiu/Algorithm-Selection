import os
import uuid
from flask import request
from flask_restful import Resource


class Upload(Resource):
    def post(self):
        file = request.files.get('file')
        file_uuid = str(uuid.uuid4())

        os.makedirs("../files", exist_ok=True)
        file.save(f"../files/{file_uuid}")

        print(f"[x] Uploaded file {file.filename}", flush=True)

        return file_uuid, 200

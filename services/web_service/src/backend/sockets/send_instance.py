import json
from flask import request
from pubsub.instance_publisher import InstancePublisher


class SendInstance:
    @staticmethod
    def send_instance(instance_json):
        print(f'[{request.sid}] Received instance: {json.dumps(instance_json)}', flush=True)

        InstancePublisher().send(json.dumps(instance_json))

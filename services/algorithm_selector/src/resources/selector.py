from flask import request
from flask_restful import Resource
from pubsub.instance_publisher import InstancePublisher


class Selector(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        instance = str(request.get_data())

        InstancePublisher().send(instance)

        return 200

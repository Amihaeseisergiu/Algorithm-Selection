import os
from flask import request
from flask_restful import Resource
from pubsub.publisher import Publisher


class Selector(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        instance = str(request.get_data())

        instances_topic = os.environ["INSTANCES_TOPIC"]
        Publisher(instances_topic).send(instance)

        return 200

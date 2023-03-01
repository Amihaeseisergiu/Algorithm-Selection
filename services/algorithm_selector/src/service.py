import os
from flask import Flask
from utils.publisher import Publisher
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Selector(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self, instance):
        instances_exchange = os.environ["INSTANCES_EXCHANGE"]
        Publisher.publish(instances_exchange, instance)

        return instance, 200


api.add_resource(Selector, '/', '/select/<instance>')


if __name__ == '__main__':
    app.run(debug=True)

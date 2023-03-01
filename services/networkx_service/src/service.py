import os
from flask import Flask
from utils.consumer import Consumer
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'message': "hello there"}


api.add_resource(HelloWorld, '/')


def callback(self, channel, method, properties, body):
    print(f"[x] {self.name} received {body}", flush=True)


if __name__ == '__main__':
    instances_exchange = os.environ["INSTANCES_EXCHANGE"]
    Consumer(instances_exchange, callback).start()

    host = os.environ["FLASK_RUN_HOST"]
    port = int(os.environ["FLASK_RUN_PORT"])
    app.run(debug=True, host=host, port=port)

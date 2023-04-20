import os
import json
import socket
import eventlet
from flask_restful import Api
from flask import Flask
from flask_socketio import SocketIO
from resources.root import Root
from resources.upload import Upload
from resources.download import Download
from pubsub.user_metric_consumer import UserMetricConsumer
from pubsub.user_algorithm_consumer import UserAlgorithmConsumer
from pubsub.instance_publisher import InstancePublisher
from pubsub.next_library_consumer import NextLibraryConsumer
from engineio.payload import Payload

Payload.max_decode_packets = 1000

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
socketio = SocketIO(app, async_mode='eventlet')
eventlet.monkey_patch()
api = Api(app)

api.add_resource(Root, '/')
api.add_resource(Upload, '/upload')
api.add_resource(Download, "/download/<file_id>")


@socketio.on("register_socket")
def register_socket(socket_id):
    UserMetricConsumer(socketio, socket_id).consume()
    UserAlgorithmConsumer(socketio, socket_id).consume()
    NextLibraryConsumer(socket_id).consume()


@socketio.on("send_instance_parallel")
def send_instance_parallel(instance_json):
    web_service_id = socket.gethostname()
    instance_json['web_service_id'] = web_service_id

    InstancePublisher(os.environ["INSTANCES_SELECTOR_KEY"]).send(json.dumps(instance_json))
    InstancePublisher(os.environ["INSTANCES_PARALLEL_KEY_PREFIX"]).send(json.dumps(instance_json))


@socketio.on("send_instance_sequential")
def send_instance_sequential(instance_json):
    socker_id = instance_json['socket_id']

    web_service_id = socket.gethostname()
    instance_json['web_service_id'] = web_service_id
    InstancePublisher(os.environ["INSTANCES_SELECTOR_KEY"]).send(json.dumps(instance_json))

    available_libraries = os.environ["LIBRARY_NAMES"].split(',')

    for library_name in available_libraries:
        schedule_data = {
            "header": {
                "library_name": library_name
            }
        }
        socketio.emit("schedule", schedule_data, to=socker_id)

    first_library = os.environ["SEQUENTIAL_LIBRARY_NAMES"].split(',')[0]
    routing_key = f"{os.environ['INSTANCES_SEQUENTIAL_KEY_PREFIX']}.{first_library}"
    instance_json['current_library'] = 0

    InstancePublisher(routing_key).send(json.dumps(instance_json))


if __name__ == '__main__':
    host = os.environ["FLASK_RUN_HOST"]
    port = int(os.environ["FLASK_RUN_PORT"])
    socketio.run(app=app, debug=True, host=host, port=port, use_reloader=False)

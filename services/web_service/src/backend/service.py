import os
import json
import eventlet
from flask_restful import Api
from flask import Flask
from flask_socketio import SocketIO
from resources.root import Root
from resources.upload import Upload
from resources.download import Download
from pubsub.user_metric_consumer import UserMetricConsumer
from pubsub.instance_publisher import InstancePublisher
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


@socketio.on("send_instance")
def send_instance(instance_json):
    InstancePublisher().send(json.dumps(instance_json))


if __name__ == '__main__':
    host = os.environ["FLASK_RUN_HOST"]
    port = int(os.environ["FLASK_RUN_PORT"])
    socketio.run(app=app, debug=True, host=host, port=port, use_reloader=False)

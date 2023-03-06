import os
import eventlet
from flask_restful import Api
from flask import Flask
from flask_socketio import SocketIO
from resources.root import Root
from sockets.register import Register
from sockets.send_instance import SendInstance
from pubsub.algorithm_consumer import AlgorithmConsumer

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
socketio = SocketIO(app, async_mode='eventlet')
eventlet.monkey_patch()
api = Api(app)

api.add_resource(Root, '/')
socketio.on_event("register", Register.register)
socketio.on_event("send_instance", SendInstance.send_instance)


if __name__ == '__main__':
    AlgorithmConsumer(socketio).consume()

    host = os.environ["FLASK_RUN_HOST"]
    port = int(os.environ["FLASK_RUN_PORT"])
    socketio.run(app=app, debug=True, host=host, port=port, use_reloader=False)

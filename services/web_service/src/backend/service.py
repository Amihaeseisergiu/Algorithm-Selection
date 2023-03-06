import os
import uuid
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on('send_instance')
def receive_instance(instance_json):
    print(f'[{request.sid}] Received instance: {str(instance_json)}', flush=True)

    emit("send_instance", instance_json, to=request.sid)


def register_callback():
    print(f"[x] Callback register received", flush=True)


@socketio.on('register')
def register():
    response = {
        "id": str(uuid.uuid4())
    }
    print('[x] Received register: ' + str(response), flush=True)
    emit('register', response, callback=register_callback)


if __name__ == '__main__':
    host = os.environ["FLASK_RUN_HOST"]
    port = int(os.environ["FLASK_RUN_PORT"])

    socketio.run(app=app, debug=True, host=host, port=port, use_reloader=False)

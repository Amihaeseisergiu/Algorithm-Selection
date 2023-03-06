import uuid
from flask_socketio import emit


class Register:
    @staticmethod
    def __register_callback():
        print(f"[x] Callback register received", flush=True)

    @staticmethod
    def register():
        response = {
            "id": str(uuid.uuid4())
        }
        print('[x] Received register: ' + str(response), flush=True)
        emit('register', response, callback=Register.__register_callback)

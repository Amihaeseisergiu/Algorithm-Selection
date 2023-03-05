import os
from flask import Flask
from flask_restful import Api
from resources.root import Root
from pubsub.instance_consumer import InstanceConsumer

app = Flask(__name__)
api = Api(app)


api.add_resource(Root, '/')


if __name__ == '__main__':
    InstanceConsumer().consume()

    host = os.environ["FLASK_RUN_HOST"]
    port = int(os.environ["FLASK_RUN_PORT"])
    app.run(debug=True, host=host, port=port, use_reloader=False)

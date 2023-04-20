import os
from flask import Flask
from resources.root import Root
from flask_restful import Api
from pubsub.instance_consumer import InstanceConsumer
from pubsub.dataset_entry_consumer import DatasetEntryConsumer

app = Flask(__name__)
api = Api(app)


api.add_resource(Root, '/')


if __name__ == '__main__':
    InstanceConsumer().consume()
    DatasetEntryConsumer().consume()

    host = os.environ["FLASK_RUN_HOST"]
    port = int(os.environ["FLASK_RUN_PORT"])
    app.run(debug=True, host=host, port=port, use_reloader=False)

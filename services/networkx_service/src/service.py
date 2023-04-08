import os
from flask import Flask
from flask_restful import Api
from resources.root import Root
from pubsub.parallel_instance_consumer import ParallelInstanceConsumer
from pubsub.sequential_instance_consumer import SequentialInstanceConsumer

app = Flask(__name__)
api = Api(app)


api.add_resource(Root, '/')


if __name__ == '__main__':
    ParallelInstanceConsumer().consume()
    SequentialInstanceConsumer().consume()

    host = os.environ["FLASK_RUN_HOST"]
    port = int(os.environ["FLASK_RUN_PORT"])
    app.run(debug=True, host=host, port=port, use_reloader=False)

import os
from flask import Flask
from resources.selector import Selector
from pubsub.algorithm_consumer import AlgorithmConsumer
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


api.add_resource(Selector, '/', '/select')


if __name__ == '__main__':
    AlgorithmConsumer().consume()

    host = os.environ["FLASK_RUN_HOST"]
    port = int(os.environ["FLASK_RUN_PORT"])
    app.run(debug=True, host=host, port=port, use_reloader=False)

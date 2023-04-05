import os
from flask import Flask
from resources.root import Root
from pubsub.selector_algorithm_consumer import SelectorAlgorithmConsumer
from pubsub.selector_metric_consumer import SelectorMetricConsumer
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


api.add_resource(Root, '/')


if __name__ == '__main__':
    SelectorAlgorithmConsumer().consume()
    SelectorMetricConsumer().consume()

    host = os.environ["FLASK_RUN_HOST"]
    port = int(os.environ["FLASK_RUN_PORT"])
    app.run(debug=True, host=host, port=port, use_reloader=False)

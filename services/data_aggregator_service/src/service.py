import os
from flask import Flask
from resources.root import Root
from repository.database import Database
from pubsub.algorithms_data_consumer import AlgorithmsDataConsumer
from pubsub.instance_features_consumer import InstanceFeaturesConsumer
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


api.add_resource(Root, '/')


@app.route("/algorithms")
def algorithms():
    algorithms_aggregations_collection = Database.get("data")["algorithms-data"]

    return list(algorithms_aggregations_collection.find(
        filter={},
        projection={"_id": 0}
    ))


@app.route("/winners")
def winners():
    libraries_winners_collection = Database.get("data")["libraries-winners"]

    return list(libraries_winners_collection.find(
        filter={},
        projection={"_id": 0}
    ))


@app.route("/dataset")
def dataset():
    dataset_collection = Database.get("data")["dataset"]

    return list(dataset_collection.find(
        filter={},
        projection={"_id": 0}
    ))


if __name__ == '__main__':
    AlgorithmsDataConsumer().consume()
    InstanceFeaturesConsumer().consume()

    host = os.environ["FLASK_RUN_HOST"]
    port = int(os.environ["FLASK_RUN_PORT"])
    app.run(debug=True, host=host, port=port, use_reloader=False)
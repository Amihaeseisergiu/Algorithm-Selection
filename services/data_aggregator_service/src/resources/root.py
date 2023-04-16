from repository.database import Database
from flask_restful import Resource


class Root(Resource):
    def get(self):
        algorithms_aggregations = Database.get("data")["algorithms-data"]

        return list(algorithms_aggregations.find(
            filter={},
            projection={"_id": 0}
        ))

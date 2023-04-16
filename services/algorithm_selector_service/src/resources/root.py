from flask_restful import Resource


class Root(Resource):
    def get(self):
        return "Unimplemented", 501

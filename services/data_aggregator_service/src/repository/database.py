import os
from pymongo import MongoClient


class Database:
    @staticmethod
    def get(database_name):
        uri = f"mongodb://{os.environ['MONGODB_USERNAME']}:{os.environ['MONGODB_PASSWORD']}@" \
              f"{os.environ['MONGODB_HOSTNAME']}:27017/"

        client = MongoClient(uri)

        return client[database_name]

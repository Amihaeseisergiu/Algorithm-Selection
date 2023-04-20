import os
from weaviate import Client


class Database:
    uri = f"http://{os.environ['WEAVIATE_HOST_NAME']}:8080/"
    client = Client(uri)

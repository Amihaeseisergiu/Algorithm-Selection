from .database import Database


class Schema:

    @staticmethod
    def create_algorithm_type_schema(algorithm_type):
        schema_class = {
            "class": algorithm_type.capitalize(),
            "description": "Shortest path vector space",
            "properties": [
                {
                    "dataType": ["text"],
                    "description": "The algorithm name",
                    "name": "algorithm",
                },
                {
                    "dataType": ["text"],
                    "description": "The algorithm library",
                    "name": "library",
                }
            ],
            "vectorizer": "none",
        }

        if not Database.client.schema.contains(schema_class):
            Database.client.schema.create_class(schema_class)

        return schema_class['class']

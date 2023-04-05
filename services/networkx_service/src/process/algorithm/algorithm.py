class Algorithm:
    def __init__(self, instance, algorithm_name, file_id):
        self.instance = instance
        self.algorithm_name = algorithm_name
        self.file_id = file_id

    def run(self):
        raise NotImplementedError("Unimplemented method")

class Algorithm:
    def __init__(self, instance, publishers):
        self.graph = instance.graph
        self.parameters = instance.parameters
        self.publishers = publishers

    def algorithm(self):
        raise NotImplementedError("Unimplemented method")

    def run(self):
        result = self.algorithm()
        self.__publish_result(result)

    def __publish_result(self, result):
        for publisher in self.publishers:
            publisher.send(result)

import os
import sys
from threading import Thread

class Algorithm:
    def __init__(self, instance, publishers):
        self.graph = instance.graph
        self.parameters = instance.parameters
        self.publishers = publishers

        self.best_heuristic_score = sys.float_info.max
        self.best_result = sys.float_info.max

    def algorithm(self):
        raise NotImplementedError("Unimplemented method")

    def run(self):
        thread = Thread(target=self.algorithm)
        thread.start()
        thread.join(timeout=int(os.environ["ALGORITHM_TIMEOUT"]))

        self.__publish_result(self.best_result, self.best_heuristic_score)

    def __publish_result(self, result, heuristic_score):
        for publisher in self.publishers:
            publisher.send(
                {
                    "result": result,
                    "heuristic_score": heuristic_score
                }
            )

import time
from metrics.profiler import Profiler


class Runner:
    def __init__(self, socket_id, algorithm_name):
        self.algorithm_name = algorithm_name
        self.profiler = Profiler(socket_id, algorithm_name)

    def run(self, data):
        self.profiler.start()

        memory = []
        for _ in range(10):
            time.sleep(1)
            memory.append("aaaaaaaaaaaaaaa" * 100000)

        return self.profiler.stop()

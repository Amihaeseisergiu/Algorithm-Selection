import time
from metrics.profiler import Profiler


class Runner:
    def __init__(self):
        self.profiler = Profiler()

    def run_and_get_metrics(self, data):
        self.profiler.start()

        memory = []
        for _ in range(10):
            time.sleep(1)
            memory.append("aaaaaaaaaaaaaaa" * 100000)

        return self.profiler.stop_and_get_metrics()

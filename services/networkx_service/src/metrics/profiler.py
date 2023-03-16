import os
import json
import psutil
from threading import Thread
from pubsub.algorithm_publisher import AlgorithmPublisher
from network.envelope import Envelope


class Profiler:
    def __init__(self, socket_id, algorithm_name, interval=0.1):
        self.socket_id = socket_id
        self.algorithm_name = algorithm_name
        self.interval = interval
        self.stopped = None

        self.initial_memory = None
        self.initial_cpu = None

        self.emitted_data_points = 0

    def get_memory(self):
        process = psutil.Process(os.getpid())
        return process.memory_info().rss

    def get_cpu(self):
        process = psutil.Process(os.getpid())
        return process.cpu_percent(interval=self.interval)

    def __emit_metrics(self, emit_state):
        current_memory = (self.get_memory() - self.initial_memory) / (1024 ** 2)
        current_cpu = self.get_cpu()

        metrics = {
            "memory": current_memory,
            "cpu": current_cpu
        }

        envelope = Envelope.create_end_user_envelope(socket_id=self.socket_id, event_name="metric_emit")
        envelope["payload"] = {
            "algorithm_name": self.algorithm_name,
            "emit_state": emit_state,
            "metrics": metrics
        }

        AlgorithmPublisher(self.socket_id).send(json.dumps(envelope))

    def __monitor(self):
        while not self.stopped:
            self.__emit_metrics("intermediate")
            # time.sleep(self.interval) # cpu_percent is blocking
            self.emitted_data_points += 1

        self.__emit_metrics("end")

    def start(self):
        self.stopped = False
        self.emitted_data_points = 0
        self.initial_memory = self.get_memory()
        self.initial_cpu = self.get_cpu()

        thread = Thread(target=self.__monitor)
        thread.start()

    def stop(self):
        self.stopped = True

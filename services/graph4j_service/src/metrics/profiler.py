import time
import json
import psutil
import multiprocessing
from threading import Thread
from pubsub.algorithm_publisher import AlgorithmPublisher
from network.envelope import Envelope


class Profiler:
    def __init__(self, socket_id, algorithm_name, interval=0.1):
        self.socket_id = socket_id
        self.algorithm_name = algorithm_name
        self.interval = interval

        self.stopped = None
        self.pid = None
        self.initial_memory = None
        self.last_memory = None
        self.max_memory = None
        self.initial_cpu = None
        self.last_cpu = None
        self.max_cpu = None
        self.initial_time = None

        self.emitted_data_points = 0

    def get_memory(self):
        process = psutil.Process(self.pid)
        return process.memory_info().rss

    def get_cpu(self):
        process = psutil.Process(self.pid)
        return process.cpu_percent(interval=self.interval) / multiprocessing.cpu_count()

    def get_time(self):
        return time.time() - self.initial_time

    def __emit_metrics(self):
        current_memory = (self.get_memory() - self.initial_memory) / (1024 ** 2)
        current_cpu = self.get_cpu()

        if current_memory < 0:
            current_memory = self.last_memory
        else:
            self.last_memory = current_memory

        if current_cpu < 0:
            current_cpu = self.last_cpu
        else:
            self.last_cpu = current_cpu

        self.max_memory = max(self.max_memory, current_memory)
        self.max_cpu = max(self.max_cpu, current_cpu)

        metrics = {
            "memory": current_memory,
            "cpu": current_cpu,
        }

        current_time = self.get_time()

        envelope = Envelope.create_end_user_envelope(socket_id=self.socket_id, event_name="metric_emit")
        envelope["payload"] = {
            "algorithm_name": self.algorithm_name,
            "metrics": metrics,
            "time": current_time
        }

        AlgorithmPublisher(self.socket_id).send(json.dumps(envelope))

    def __end_metrics(self):
        metrics = {
            "memory": self.max_memory,
            "cpu": self.max_cpu,
        }

        current_time = self.get_time()

        envelope = Envelope.create_end_user_envelope(socket_id=self.socket_id, event_name="metric_end")
        envelope["payload"] = {
            "algorithm_name": self.algorithm_name,
            "metrics": metrics,
            "time": current_time
        }

        AlgorithmPublisher(self.socket_id).send(json.dumps(envelope))

    def __monitor(self):
        while not self.stopped:
            try:
                self.__emit_metrics()
            except:
                self.stopped = True
                break

            self.emitted_data_points += 1

        self.__end_metrics()

    def start(self, pid):
        self.pid = pid
        self.stopped = False
        self.emitted_data_points = 0
        self.initial_memory = self.last_memory = self.max_memory = self.get_memory()
        self.initial_cpu = self.last_cpu = self.max_cpu = self.get_cpu()
        self.initial_time = time.time()

        thread = Thread(target=self.__monitor)
        thread.start()

    def stop(self):
        self.stopped = True

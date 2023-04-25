import os
import gc
import time
import psutil
import multiprocessing
from threading import Thread
from pubsub.user_publisher import UserPublisher
from pubsub.algorithms_data_publisher import AlgorithmsDataPublisher


class Profiler:
    def __init__(self, socket_id, file_id, algorithm_name, algorithm_type):
        self.socket_id = socket_id
        self.file_id = file_id
        self.algorithm_name = algorithm_name
        self.algorithm_type = algorithm_type

        self.initialized = False
        self.initialized_memory_set = False
        self.stopped = False
        self.emitted_data_points = 1

        self.total_memory = 0
        self.total_cpu = 0
        self.last_recorded_time = None
        self.initialization_memory = 0

        self.start_time = None

    def get_memory(self):
        process = psutil.Process(os.getpid())
        return process.memory_info().rss / 1024 / 1024

    def get_cpu(self):
        process = psutil.Process(os.getpid())
        return process.cpu_percent(interval=0.1) / multiprocessing.cpu_count()

    def get_time(self):
        return time.time() - self.start_time

    def __emit(self):
        current_memory = self.get_memory() - self.initialization_memory
        current_cpu = self.get_cpu()
        current_time = self.get_time()

        if self.initialized and current_memory >= 0:
            self.total_memory += current_memory
            self.total_cpu += current_cpu
            self.emitted_data_points += 1

        if self.initialized and (not self.initialized_memory_set or current_memory < 0):
            self.initialization_memory = self.get_memory()
            self.initialized_memory_set = True

            if current_memory < 0:
                current_memory = self.initialization_memory
            else:
                current_memory = 0

        self.last_recorded_time = current_time

        user_data = {
            "event_name": "metric_emit",
            "payload": {
                "algorithm_name": self.algorithm_name,
                "metrics": {
                    "memory": current_memory,
                    "cpu": current_cpu,
                },
                "time": current_time
            }
        }

        UserPublisher(self.socket_id, self.algorithm_name).send(user_data)

    def __post_emit(self):
        user_data = {
            "event_name": "metric_end",
            "payload": {
                "algorithm_name": self.algorithm_name,
                "time": self.last_recorded_time
            }
        }

        UserPublisher(self.socket_id, self.algorithm_name).send(user_data)

        data_aggregator_features = {
            "avg_memory": self.total_memory / self.emitted_data_points,
            "avg_cpu": self.total_cpu / self.emitted_data_points,
            "total_time": self.last_recorded_time
        }

        AlgorithmsDataPublisher(self.file_id, self.algorithm_name, self.algorithm_type).send(data_aggregator_features)

    def __monitor(self):
        self.start_time = time.time()

        while not self.stopped:
            try:
                self.__emit()
            except Exception as e:
                self.stopped = True
                break

        self.__post_emit()

    def mark_initialization(self):
        gc.collect()
        gc.disable()
        self.initialized = True

    def start(self):
        Thread(target=self.__monitor).start()

    def stop(self):
        self.stopped = True

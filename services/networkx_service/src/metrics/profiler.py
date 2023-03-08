import os
import time
import psutil
from threading import Thread


class Profiler:
    def __init__(self):
        self.memory_data_points = None
        self.initial_memory = None

        self.cpu_data_points = None
        self.initial_cpu = None

        self.stopped = None

    def get_memory(self):
        process = psutil.Process(os.getpid())
        return process.memory_info().rss

    def get_cpu(self):
        process = psutil.Process(os.getpid())
        return process.cpu_percent()

    def __monitor(self):
        while not self.stopped:
            current_memory = (self.get_memory() - self.initial_memory) / (1024 ** 2)
            current_cpu = self.get_cpu() - self.initial_cpu

            print(f"[x] Current memory {current_memory} | Current CPU {current_cpu}", flush=True)

            self.memory_data_points.append(current_memory)
            self.cpu_data_points.append(current_cpu)

            time.sleep(1)

    def start(self):
        self.memory_data_points = []
        self.initial_memory = self.get_memory()

        self.cpu_data_points = []
        self.initial_cpu = self.get_cpu()

        self.stopped = False
        thread = Thread(target=self.__monitor)
        thread.start()

    def stop(self):
        self.stopped = True

    def stop_and_get_metrics(self):
        self.stop()

        return {
            "memory": self.memory_data_points,
            "cpu": self.cpu_data_points
        }

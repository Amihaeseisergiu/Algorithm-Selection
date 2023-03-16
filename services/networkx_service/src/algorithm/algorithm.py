import math
from threading import Thread
from multiprocessing import Process
from metrics.profiler import Profiler


class Algorithm:
    def __init__(self, socket_id, algorithm_name, runnable_algorithm):
        self.algorithm_name = algorithm_name
        self.profiler = Profiler(socket_id, algorithm_name)
        self.runnable_algorithm = runnable_algorithm

    def __run_algorithm(self, data):
        self.runnable_algorithm(data)

    def __run_callback(self, data):
        self.profiler.start()

        process = Process(target=self.__run_algorithm, args=(data,))
        process.start()
        process.join()

        self.profiler.stop()

    def run(self, data):
        thread = Thread(target=self.__run_callback, args=(data,))
        thread.start()

        return thread

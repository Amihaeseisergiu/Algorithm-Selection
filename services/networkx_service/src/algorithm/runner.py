import math
from threading import Thread
from multiprocessing import Process
from metrics.profiler import Profiler


class AlgorithmRunner:
    def __init__(self, socket_id, algorithm_name):
        self.algorithm_name = algorithm_name
        self.profiler = Profiler(socket_id, algorithm_name)

    def __run_algorithm(self, data):
        memory = []
        for i in range(10):
            for j in range(10):
                math.factorial(i ** 5)
            memory.append("aaaaaaaaaaaaaaa" * 100000)

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

from threading import Thread
import subprocess
from metrics.profiler import Profiler


class Algorithm:
    def __init__(self, socket_id, algorithm_name, runnable_algorithm):
        self.algorithm_name = algorithm_name
        self.profiler = Profiler(socket_id, algorithm_name)
        self.runnable_algorithm = runnable_algorithm

    def __run_algorithm(self, data):
        self.runnable_algorithm(data)

    def __run_callback(self, data):
        process = subprocess.Popen(["java", "-jar", "/process/process.jar", "test"])

        self.profiler.start(process.pid)

        process.wait()

    def run(self, data):
        thread = Thread(target=self.__run_callback, args=(data,))
        thread.start()

        return thread

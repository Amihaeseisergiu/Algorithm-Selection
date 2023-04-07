from threading import Thread
from metrics.profiler import Profiler


class Algorithm:
    def __init__(self, socket_id, file_id, algorithm_name, runnable_algorithm):
        self.socket_id = socket_id
        self.file_id = file_id
        self.algorithm_name = algorithm_name
        self.profiler = Profiler(socket_id, file_id, algorithm_name)
        self.runnable_algorithm = runnable_algorithm

    def __run_algorithm(self, instance_path):
        return self.runnable_algorithm(instance_path)

    def __run_callback(self, instance_path):
        process = self.__run_algorithm(instance_path)

        self.profiler.start(process.pid)

        process.wait()

    def create(self, instance_path):
        thread = Thread(target=self.__run_callback, args=(instance_path,))
        return thread

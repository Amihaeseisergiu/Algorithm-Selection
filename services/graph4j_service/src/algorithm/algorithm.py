import time
import subprocess
from threading import Thread


class Algorithm:
    def __init__(self, socket_id, file_id, algorithm_name, algorithm_type):
        self.socket_id = socket_id
        self.file_id = file_id
        self.algorithm_name = algorithm_name
        self.algorithm_type = algorithm_type

    def __run_algorithm(self, instance_path):
        return subprocess.Popen(["java", "-jar", "-Xmx8192m", "/process/process.jar",
                                 instance_path, self.algorithm_name, self.algorithm_type,
                                 self.file_id, self.socket_id, str(time.time())])

    def __run_callback(self, instance_path):
        process = self.__run_algorithm(instance_path)
        process.wait()

    def create(self, instance_path):
        thread = Thread(target=self.__run_callback, args=(instance_path,))
        return thread

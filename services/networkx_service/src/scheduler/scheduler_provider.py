from scheduler.shortest_path import ShortestPathScheduler


class SchedulerProvider:
    def __init__(self, socket_id, file_id):
        self.schedulers = {
            "shortest_path": ShortestPathScheduler(socket_id, file_id)
        }

    def get(self, algorithm_type):
        return self.schedulers[algorithm_type]

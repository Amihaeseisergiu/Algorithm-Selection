from scheduler.shortest_path import ShortestPathScheduler


class SchedulerProvider:
    def __init__(self, socket_id):
        self.schedulers = {
            "shortest_path": ShortestPathScheduler(socket_id)
        }

    def get(self, algorithm_type):
        return self.schedulers[algorithm_type]

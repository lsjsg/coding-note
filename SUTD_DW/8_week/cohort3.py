import time
class StopWatch:
    def __init__(self):
        self.start_time = time.time()
        self.end_time = -1.0
    def start(self):
        self.start_time = time.time()
        self.end_time = -1.0
    def stop(self):
        self.end_time = time.time()
    def elapsed_time(self):
        return round(float(self.end_time - self.start_time),1) if self.end_time > 0 else None

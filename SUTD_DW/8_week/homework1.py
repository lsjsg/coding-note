class Time:
    def __init__(self,hour,minutes,seconds):
        self._hours = hour
        self._minutes = minutes
        self._seconds = seconds
    def getter(self):
        return (self._seconds - 0) + 60*(self._minutes - 0) + 3600*(self._hours - 0)
    def setter(self,elapsed_time):
        elapsed_time %= 86400
        self._hours = elapsed_time // 3600
        self._minutes = (elapsed_time%3600) // 60
        self._seconds = (elapsed_time%60)
    def __str__(self):
        return "Time: {0}:{1}:{2}".format(self._hours,self._minutes,self._seconds)
    elapsed_time = property(fget=getter,fset=setter)
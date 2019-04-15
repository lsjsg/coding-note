class Diff:
    def __init__(self,function,h=1e-4):
        self.function = function
        self.h = h
    def __call__(self,x):
        return (self.function(x + self.h) - self.function(x)) / self.h
    
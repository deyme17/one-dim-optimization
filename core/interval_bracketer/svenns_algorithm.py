from utils import IIntervalBracketer

class SvennsAlgorithm(IIntervalBracketer):
    def find_interval(self, obj_func, x_0 = 0, h = 0.1):
        return super().find_interval(obj_func, x_0, h)
from utils import IOptimizer

class GoldenSectionMethod(IOptimizer):
    def optimize(self, obj_func, interval_result, epsilon = 0.001):
        return super().optimize(obj_func, interval_result, epsilon)
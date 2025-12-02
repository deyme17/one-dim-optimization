from utils import IOptimizer

class FibonacciMethod(IOptimizer):
    def optimize(self, obj_func, interval_result, epsilon = 0.001):
        return super().optimize(obj_func, interval_result, epsilon)
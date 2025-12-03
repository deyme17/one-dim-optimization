from utils import IIntervalBracketer, IntervalResult
from typing import Callable

class SvennsAlgorithm(IIntervalBracketer):
    """Implementation of the Svenn's algorithm for finding uncertainty interval"""
    MAX_ITER = 1e5
    def find_interval(self, obj_func: Callable[[float], float], x_0: float = 0, h: float = 0.1) -> IntervalResult:
        """
        Determines the uncertainty interval [a, b] for a unimodal function.
        Args:
            obj_func (Callable[[float], float]): The objective function f(x).
            x_0 (float): The starting point for the search.
            h (float): The initial step. Defaults to 0.1.
        Returns: Interval Result with fileds:
            - interval: Tuple[float, float],
            - internal_point: float,
            - values: Tuple[float, float, float]
        """
        a = c = b = None
        x = x_0
        y = obj_func(x_0)

        k = 0
        while a is None and b is None:
            if k > self.MAX_ITER: return
            
            new_x = x + 2**k * h
            new_y = obj_func(new_x)

            if new_y < y:
                a = x
                c = new_x
                y = new_y
                x = new_x
            else:
                if h > 0:
                    a = x_0
                    b = new_x
                else:
                    a = new_x
                    b = x_0
                c = x
                break
            k += 1

        return IntervalResult(
            interval=(a, b),
            internal_point=c,
            values=(obj_func(a), 
                    obj_func(c), 
                    obj_func(b))
        )
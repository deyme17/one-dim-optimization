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
        Returns: Interval Result with fields:
            - interval: Tuple[float, float],
            - internal_point: float,
            - values: Tuple[float, float, float]
        """
        x_prev = x_0
        f_prev = obj_func(x_0)
        
        x_curr = x_0 + h
        f_curr = obj_func(x_curr)
        
        if f_curr < f_prev:
            step = h
        else:
            step = -h
            x_prev, x_curr = x_curr, x_prev
            f_prev, f_curr = f_curr, f_prev
        
        k = 1
        while k < self.MAX_ITER:
            x_new = x_0 + (2**k) * step
            f_new = obj_func(x_new)
            
            if f_new >= f_curr:
                if step > 0:
                    a = x_prev
                    b = x_new
                    c = x_curr
                else:
                    a = x_new
                    b = x_prev
                    c = x_curr
                
                return IntervalResult(
                    interval=(a, b),
                    internal_point=c,
                    values=(obj_func(a), obj_func(c), obj_func(b))
                )
            x_prev = x_curr
            f_prev = f_curr
            x_curr = x_new
            f_curr = f_new
            k += 1
        
        raise RuntimeError(f"Maximum iterations ({self.MAX_ITER}) reached without finding interval")
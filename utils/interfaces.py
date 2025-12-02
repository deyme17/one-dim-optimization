from typing import Dict, Tuple, Any, Callable
from .containers import IntervalResult, OptimizationResult
from abc import ABC, abstractmethod


class IIntervalBracketer(ABC):
    """Class-interface for finding interval [a, b] with unimodal function for further optimization (1-D)."""
    @abstractmethod
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
        pass


class IOptimizer(ABC):
    """
    Class-interface for one-dimensional optimization.
    """
    @abstractmethod
    def optimize(self, obj_func: Callable[[float], float], interval_result: IntervalResult, epsilon: float = 0.001) -> OptimizationResult:
        """
        Calculating the function optimum (minimium) from uncertainty interval with internal point and its values.
        Args:
            obj_func (Callable[[float], float]): The objective function f(x) to minimize.
            interval_result (IntervalResult): Uncertainty interval with internal point and its values.
            epsilon (float): Optimization pricision. Defaults to 0.001.
        Returns: OptimizationResult with fields:
            - x_min: float
            - value: float
            - iterations: int
            - final_epsilon: float        
        """
        pass
from utils import (
    IOptimizer, IntervalResult, OptimizationResult, 
    SolutionStatus
)
from typing import Callable

class GoldenSectionMethod(IOptimizer):
    """Implementation of golden section method for single-variable optimization"""
    # Golden ratio constants: phi = (sqrt(5) - 1) / 2 ~ 0.618
    GOLDEN_RATIO_1 = 0.3819660112 # 1 - phi
    GOLDEN_RATIO_2 = 0.6180339888 # phi

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
        if interval_result is None:
            return OptimizationResult(
                status=SolutionStatus.NOT_CONVERGED.value
            )
        a, b = interval_result.interval
        iterations = 0
        
        x1 = a + self.GOLDEN_RATIO_1 * (b - a)
        x2 = a + self.GOLDEN_RATIO_2 * (b - a)
        f1 = obj_func(x1)
        f2 = obj_func(x2)
        
        while (b - a) > epsilon:
            if f1 < f2:
                b = x2
                x2 = x1
                f2 = f1
                x1 = a + self.GOLDEN_RATIO_1 * (b - a)
                f1 = obj_func(x1)
            else:
                a = x1
                x1 = x2
                f1 = f2
                x2 = a + self.GOLDEN_RATIO_2 * (b - a)
                f2 = obj_func(x2)
            
            iterations += 1

        x_min = (a + b) / 2
        value = obj_func(x_min)
        
        return OptimizationResult(
            x_min=x_min,
            value=value,
            iterations=iterations,
            final_epsilon=b - a,
            status=SolutionStatus.OPTIMAL.value
        )
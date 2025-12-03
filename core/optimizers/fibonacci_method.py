from utils import (
    IOptimizer, IntervalResult, OptimizationResult,
    SolutionStatus
)
from typing import Callable, Tuple, List


class FibonacciMethod(IOptimizer):
    """Implementation of fibonacci method for single-variable optimization"""
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
        L = b - a
        FIB, N = self._calculate_N_fibonacci(L, epsilon)

        iterations = 0

        x1 = b - FIB[N - 1] / FIB[N] * L
        x2 = a + FIB[N - 1] / FIB[N] * L
        f1 = obj_func(x1)
        f2 = obj_func(x2)

        while N > 3:
            if f1 < f2:
                b = x2
                x2 = x1
                f2 = f1
                L = b - a
                x1 = b - FIB[N - 2] / FIB[N - 1] * L
                f1 = obj_func(x1)
            else:
                a = x1
                x1 = x2
                f1 = f2
                L = b - a
                x2 = a + FIB[N - 2] / FIB[N - 1] * L
                f2 = obj_func(x2)

            N -= 1
            iterations += 1

        # N == 3
        x_min = (x1 + x2) / 2
        value = obj_func(x_min)

        return OptimizationResult(
            x_min=x_min,
            value=value,
            iterations=iterations,
            final_epsilon=b - a,
            status=SolutionStatus.OPTIMAL.value
        )
    
    def _calculate_N_fibonacci(self, L: float, epsilon: float = 0.001) -> Tuple[List[int], int]:
        """
        Calculate first N fibonacci numbers.
        Args:
            L (float): the length of the interval (a, b)
            epsilon (float): desired method pricision.
        Returns:
            Tuple: (List of the first N Fibonacci numbers,
                    Number of Fibonacci nambers)
        """
        fib = [1, 1]
        while fib[-1] < L / epsilon:
            fib.append(fib[-1] + fib[-2])
        N = len(fib) - 1
        return fib, N
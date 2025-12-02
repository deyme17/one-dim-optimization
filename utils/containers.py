from typing import Tuple, Callable
from dataclasses import dataclass

@dataclass
class OptimizationProblem:
    obj_func: Callable[[float], float]
    # opt meyhod config
    epsilon: float
    method_name: str
    # bracketer config
    bracketer_name: str
    x_0: float
    h: float

@dataclass
class IntervalResult:
    interval: Tuple[float, float]
    internal_point: float
    values: Tuple[float, float, float]

@dataclass
class OptimizationResult:
    x_min: float
    value: float
    iterations: int
    final_epsilon: float
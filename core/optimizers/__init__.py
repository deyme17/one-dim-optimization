from utils import IOptimizer

from .fibonacci_method import FibonacciMethod
from .golden_section_method import GoldenSectionMethod

optimizers: dict[str, IOptimizer] = {
    "Fibonacci method": FibonacciMethod(),
    "Golden Section method": GoldenSectionMethod(),
}
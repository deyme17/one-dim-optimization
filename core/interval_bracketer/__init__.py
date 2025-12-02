from utils import IIntervalBracketer
from .svenns_algorithm import SvennsAlgorithm

bracketers: dict[str, IIntervalBracketer] = {
    "Svenn's algorithm": SvennsAlgorithm(),
}
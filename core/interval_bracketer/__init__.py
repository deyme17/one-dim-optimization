from utils import IIntervalBracketer
from .svenns_method import SvennsMethod

bracketers: dict[str, IIntervalBracketer] = {
    "Svenn's method": SvennsMethod(),
}
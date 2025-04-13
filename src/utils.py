
from src.dice import *

class NumericOutcome:

    def __init__(self, flat: int = 1, d6s: int = 0, d3s: int = 0) -> None:
        self.flat = flat
        self.d6s = d6s
        self.d3s = d3s

    def getVal() -> int:
        vals = [self.flat]
        for _ in range(self.d6s):
            vals.append(roll_d6())
        for _ in range(self.d3s):
            vals.append(roll_d3())
        return sum(vals)

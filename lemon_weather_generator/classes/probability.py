from __future__ import annotations

import random
from .config import Config

class Probability:
    def __init__(self, min: float, max: float, mean: float = 0, deviation: float = 0):
        config = Config.get_instance()

        self.min = round(min, config.decimal_digits)
        self.max = round(max, config.decimal_digits)
        self.mean = round(mean, config.decimal_digits)
        self.deviation = round(deviation, config.decimal_digits)
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Probability):
            return (self.min == other.min
                    and self.max == other.max
                    and self.mean == other.mean
                    and self.deviation == other.deviation)
        return False

    def getFromListOrDict(values: list|dict) -> Probability:
        if type(values) == list:
            min = values[0]
            max = values[1]
            mean = (min + max) / 2
            deviation = (max - min) * 2
        else:
            min = values['min']
            max = values['max']
            mean = values['mean']
            deviation = values['deviation']

        return Probability(min, max, mean, deviation)
    
    def toList(self) -> list:
        return [self.min, self.max, self.mean, self.deviation]

    def randomize(self) -> float:
        config = Config.get_instance()
        return round(self.normalDistribution(), config.decimal_digits)

    def normalDistribution(self) -> float:
        x = random.gauss(self.mean, self.deviation)
        while x < self.min or x > self.max:  # make sure the result is within the given interval
            x = random.gauss(self.mean, self.deviation)
        return x
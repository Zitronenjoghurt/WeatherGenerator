import random

class Propability:
    def __init__(self, min: float, max: float, mean: float = 0, deviation: float = 0):
        self.min = min
        self.max = max
        self.mean = mean
        self.deviation = deviation
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Propability):
            return (self.min == other.min
                    and self.max == other.max
                    and self.mean == other.mean
                    and self.deviation == other.deviation)
        return False

    def getFromList(values: list):
        return Propability(values[0], values[1], 0, 0)

    def randomize(self):
        if self.mean == 0 and self.deviation == 0:
            return self.randomInBetween()
        else:
            return self.normalDistribution()
        
    def randomInBetween(self):
        return random.uniform(self.min, self.max)

    def normalDistribution(self):
        x = random.gauss(self.mean, self.deviation)
        while x < self.min or x > self.max:  # make sure the result is within the given interval
            x = random.gauss(self.mean, self.deviation)
        return x
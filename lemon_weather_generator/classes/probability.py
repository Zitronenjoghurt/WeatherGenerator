import random

class Probability:
    def __init__(self, min: float, max: float, mean: float = 0, deviation: float = 0):
        self.min = min
        self.max = max
        self.mean = mean
        self.deviation = deviation
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Probability):
            return (self.min == other.min
                    and self.max == other.max
                    and self.mean == other.mean
                    and self.deviation == other.deviation)
        return False

    def getFromListOrDict(values: list|dict):
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

    def randomize(self):
        return self.normalDistribution()

    def normalDistribution(self):
        x = random.gauss(self.mean, self.deviation)
        while x < self.min or x > self.max:  # make sure the result is within the given interval
            x = random.gauss(self.mean, self.deviation)
        return x
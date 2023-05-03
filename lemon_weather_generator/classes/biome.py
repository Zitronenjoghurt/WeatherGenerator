class Biome:
    def __init__(self, temperatures):
        self.temperatures = temperatures

    def __eq__(self, other):
        if isinstance(other, Biome):
            return self.temperatures == other.temperatures
        return False
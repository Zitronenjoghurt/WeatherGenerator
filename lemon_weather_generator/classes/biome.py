import random

class Biome:
    def __init__(self, name: str, temperatures: list):
        self.name = name.lower()
        self.temperatures = temperatures

    def __eq__(self, other):
        if isinstance(other, Biome):
            return (self.name == other.name and self.temperatures == other.temperatures)
        return False
    
    def randomTemperature(self, decimal_digits):
        temp = random.uniform(self.temperatures[0], self.temperatures[1])
        return round(temp, decimal_digits)
    
class Biomes:
    def __init__(self, biome_list: list[Biome]):
        self.biome_dict = {}

        for biome in biome_list:
            if biome.name not in self.biome_dict:
                self.biome_dict[biome.name] = biome

    def __getitem__(self, key):
        return self.biome_dict[key.lower()]
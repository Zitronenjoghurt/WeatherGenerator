class Biome:
    def __init__(self, name: str, temperatures: list):
        self.name = name
        self.temperatures = temperatures

    def __eq__(self, other):
        if isinstance(other, Biome):
            return (self.temperatures == other.temperatures and self.temperatures == other.temperatures)
        return False
    
class Biomes:
    def __init__(self, biome_list: list[Biome]):
        self.biomes_list = biome_list

    def findBiomeByName(self, name: str) -> Biome|None:
        result = [item for item in self.biomes_list if item.name == name.lower()]

        if len(result) != 0:
            return result[0]
        else:
            return None
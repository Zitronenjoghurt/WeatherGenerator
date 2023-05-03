from . import Config, Biomes
class Configurations:
    def __init__(self, config: Config, biomes: Biomes):
        self.config = config
        self.biomes = biomes

    def __eq__(self, other):
        if isinstance(other, Configurations):
            return (self.config == other.config and self.biomes == other.biomes)
        return False
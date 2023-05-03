from .modules import configLoader
from .classes import Configurations

def loadConfigurations() -> Configurations:
    config = configLoader.getConfig()
    biomes = configLoader.getBiomes()

    return Configurations(config, biomes)
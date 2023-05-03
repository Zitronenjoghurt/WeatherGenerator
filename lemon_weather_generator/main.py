from .modules import configLoader
from .classes import Configurations

def loadConfigurations():
    config = configLoader.getConfig()
    biomes = configLoader.getBiomes()

    return Configurations(config, biomes)
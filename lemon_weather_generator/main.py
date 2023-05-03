from .modules import configLoader

def loadConfigurations():
    config = configLoader.getConfig()
    return config
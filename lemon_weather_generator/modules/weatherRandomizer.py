from . import loadConfigurations

def randomizeWeather(biomeName: str, seasonName: str):
    Configuration = loadConfigurations()
    
    biome = Configuration.biomes[biomeName]
    return biome[seasonName].randomTemperature(Configuration.config.decimal_digits)
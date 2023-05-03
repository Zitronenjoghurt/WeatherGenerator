from . import loadConfigurations

from lemon_weather_generator.classes import Biome, Biomes

def randomizeWeather(biomeName: str):
    Configuration = loadConfigurations()
    
    biome = Configuration.biomes.findBiomeByName(biomeName)
    return biome.randomTemperature(Configuration.config.decimal_digits)
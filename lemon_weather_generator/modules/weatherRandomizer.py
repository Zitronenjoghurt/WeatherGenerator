from lemon_weather_generator.classes.config import Config
from lemon_weather_generator.classes import Biomes

def randomizeWeather(biomeName: str, seasonName: str):
    config = Config.get_instance()
    biomes = Biomes.get_instance()
    
    biome = biomes[biomeName]
    return biome[seasonName].randomTemperature(config.decimal_digits)
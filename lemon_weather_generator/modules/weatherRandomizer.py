from lemon_weather_generator.classes import Biomes

def randomizeWeather(biomeName: str, seasonName: str):
    biomes = Biomes.get_instance()
    
    biome = biomes[biomeName]
    return biome[seasonName].randomTemperature()
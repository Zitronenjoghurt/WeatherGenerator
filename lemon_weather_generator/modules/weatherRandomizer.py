from lemon_weather_generator.classes import Configurations

def randomizeWeather(biomeName: str, seasonName: str):
    Configuration = Configurations.get_instance()
    
    biome = Configuration.biomes[biomeName]
    return biome[seasonName].randomTemperature(Configuration.config.decimal_digits)
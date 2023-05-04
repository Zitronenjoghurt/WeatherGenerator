import json
import os

from lemon_weather_generator.classes import Biome, Biomes, Config, Configurations, Season, Seasons

config_path = os.path.join(os.path.dirname(__file__), '..', 'configurations')

biome_path = config_path + "\\biomes"
biome_files = [f for f in os.listdir(biome_path) if f.endswith('.json')]

def loadConfigurations() -> Configurations:
    config = getConfig()
    biomes = getBiomes()

    return Configurations(config, biomes)

def getConfig() -> Config:
    with open(config_path + "\\config.json", 'r') as f:
        data = json.load(f)
    return Config(**data)

def getBiomes() -> Biomes:
    biomes = []
    for file in biome_files:
        # get JSON from biome file
        with open(biome_path + "\\" + file, 'r') as f:
            data = json.load(f)

        # instantiate biome and append to biome list
        biomes.append(Biome(**data))
        
    return Biomes(biomes)
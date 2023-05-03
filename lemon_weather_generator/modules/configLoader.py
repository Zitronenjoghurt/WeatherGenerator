import json
import os

from lemon_weather_generator.classes import Biome, Config

config_path = os.path.join(os.path.dirname(__file__), '..', 'configurations')

biome_path = config_path + "\\biomes"
biome_files = [f for f in os.listdir(biome_path) if f.endswith('.json')]

def getConfig() -> Config:
    with open(config_path + "\\config.json", 'r') as f:
        data = json.load(f)
    return Config(**data)

def getBiomes() -> list[Biome]:
    biomes = []
    for file in biome_files:
        with open(biome_path + "\\" + file, 'r') as f:
            data = json.load(f)
        biome = Biome(**data)
        biomes.append(biome)
    return biomes
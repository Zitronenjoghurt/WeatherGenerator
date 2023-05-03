from lemon_weather_generator import loadConfigurations
from lemon_weather_generator.classes import Configurations, Biome, Config

def test_loadConfigurations():
    config = Config({"temperatureCloudiness": True})
    biomes = [Biome([0, 20])]
    configurations = Configurations(config, biomes)
                                    
    assert loadConfigurations() == configurations
from lemon_weather_generator import loadConfigurations
from lemon_weather_generator.classes import *

def test_loadConfigurations():
    configurations = loadConfigurations()
    
    config = configurations.config
    biomes = configurations.biomes

    # test a selection of values
    assert config.effects['temperatureCloudiness'] == True
    assert biomes.findBiomeByName("Temperate").temperatures == [0, 20]
from lemon_weather_generator.modules import loadConfigurations

def test_loadConfigurations():
    configurations = loadConfigurations()
    
    config = configurations.config
    biomes = configurations.biomes

    # test a selection of values
    assert config.effects['temperatureCloudiness'] == True
    assert biomes['temperate'].temperatures == [0, 20]
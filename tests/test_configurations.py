from lemon_weather_generator.classes import Configurations

def test_instantiation():
    configurations = Configurations.get_instance()
    
    config = configurations.config
    biomes = configurations.biomes

    assert config.decimal_digits == 1
    assert config.hours_per_day == 24
    assert config.effects['temperatureCloudiness'] == True
    assert biomes['temperate']['spring'].temperatures.min == 10
    assert biomes['temperate']['spring'].temperatures.max == 20
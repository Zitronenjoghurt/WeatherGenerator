from lemon_weather_generator.classes import Biome, Biomes

def test_instantiation():
    biomes = Biomes.get_instance()

    assert biomes['temperate'].name == 'temperate'
    assert biomes['temperate']['summer'].temperatures.min == 20
    assert biomes['temperate']['summer'].temperatures.max == 50
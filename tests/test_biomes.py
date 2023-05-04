from lemon_weather_generator.classes import Biome, Biomes

def test_instantiation():
    biome1 = Biome('temperate', [{'name': 'spring', 'temperatures': [0, 20]}])
    biome2 = Biome('desert', [{'name': 'summer', 'temperatures': [30, 60]}])
    biome3 = Biome('arctic', [{'name': 'winter', 'temperatures': [-80, 5]}])

    biomes = Biomes([biome1, biome2, biome3])
    assert biomes['temperate'] == biome1
    assert biomes['desert'] == biome2
    assert biomes['arctic'] == biome3
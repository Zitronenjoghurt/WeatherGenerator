from lemon_weather_generator.classes import Biome, Biomes

def test_instantiation():
    biome1 = Biome('temperate', [0, 20])
    biome2 = Biome('desert', [20, 50])
    biome3 = Biome('arctic', [-80, 0])

    biomes = Biomes([biome1, biome2, biome3])
    assert biomes['temperate'] == biome1
    assert biomes['desert'] == biome2
    assert biomes['arctic'] == biome3
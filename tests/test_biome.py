from lemon_weather_generator.classes import Biome, Season, Seasons

def test_eq():
    biome1 = Biome('temperate', 'C', [{'name': 'spring', 'daytime_percentage': 50, 'temperatures': [0, 20]}])
    biome2 = Biome('temperate', 'C', [{'name': 'spring','daytime_percentage': 50, 'temperatures': [0, 20]}])
    biome3 = Biome('polar', 'C', [{'name': 'summer','daytime_percentage': 70, 'temperatures': [-10, 5]}])
    biome4 = Biome('polar', 'C', [{'name': 'winter','daytime_percentage': 30, 'temperatures': [10, 30]}])

    assert biome1 == biome2
    assert biome2 != biome3
    assert biome3 != biome4

def test_season_randomTemperature():
    biome1 = Biome('temperate', 'C', [{'name': 'winter','daytime_percentage': 30, 'temperatures': [-50, 50]}])
    biome2 = Biome('scorching_hot', 'C', [{'name': 'summer','daytime_percentage': 70, 'temperatures': [50, 150]}])

    temp1 = biome1['winter'].randomTemperature()
    assert temp1 >= -50 and temp1 <= 50
    assert str(temp1)[::-1].find('.') == 2 # two decimal places

    temp2 = biome2['summer'].randomTemperature()
    assert temp2 >= 50 and temp2 <= 150
    assert str(temp2)[::-1].find('.') == 2 # two decimal places
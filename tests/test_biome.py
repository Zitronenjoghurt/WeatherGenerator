from lemon_weather_generator.classes import Biome, Season, Seasons

def test_eq():
    biome1 = Biome('temperate', [{'name': 'spring', 'temperatures': [0, 20]}])
    biome2 = Biome('temperate', [{'name': 'spring', 'temperatures': [0, 20]}])
    biome3 = Biome('polar', [{'name': 'summer', 'temperatures': [-10, 5]}])
    biome4 = Biome('polar', [{'name': 'winter', 'temperatures': [10, 30]}])

    assert biome1 == biome2
    assert biome2 != biome3
    assert biome3 != biome4

def test_season_randomTemperature():
    biome1 = Biome('temperate', [{'name': 'winter', 'temperatures': [-50, 50]}])
    biome2 = Biome('scorching_hot', [{'name': 'summer', 'temperatures': [50, 150]}])

    temp1 = biome1['winter'].randomTemperature(1)
    assert temp1 >= -50 and temp1 <= 50
    assert str(temp1)[::-1].find('.') == 1 # one decimal place

    temp2 = biome2['summer'].randomTemperature(2)
    assert temp2 >= 50 and temp2 <= 150
    assert str(temp2)[::-1].find('.') == 2 # two decimal places
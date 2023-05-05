from lemon_weather_generator.classes import Season, Seasons, Biome

def test_instantiation():
    season = Season(None, 'SPRING', 50, [0, 20])

    assert season.name == 'spring'
    assert season.temperatures.min == 0
    assert season.temperatures.max == 20

def test_eq():
    season1 = Season(None, 'SPRING', 50, [0, 20])
    season2 = Season(None, 'sPrInG', 50, [0, 20])
    season3 = Season(None, 'summer', 70, [15, 35])
    season4 = Season(None, 'winter', 30, [-50, 0])

    assert season1 == season2
    assert season1 != season3
    assert season3 != season4

def test_randomTemperature():
    season1 = Season(Seasons(Biome('temperate', 'C')), 'summer', 70, [15, 35])
    season2 = Season(Seasons(Biome('temperate', 'C')), 'winter', 30, [-50, 0])

    temp1 = season1.randomTemperature()
    assert temp1 >= 15 and temp1 <= 35
    assert str(temp1)[::-1].find('.') == 2 # two decimal places

    temp2 = season2.randomTemperature()
    assert temp2 >= -50 and temp2 <= 0
    assert str(temp2)[::-1].find('.') == 2 # two decimal places
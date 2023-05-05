from lemon_weather_generator.classes import Season

def test_instantiation():
    season = Season('SPRING', 50, [0, 20])

    assert season.name == 'spring'
    assert season.temperatures.min == 0
    assert season.temperatures.max == 20

def test_eq():
    season1 = Season('SPRING', 50, [0, 20])
    season2 = Season('sPrInG', 50, [0, 20])
    season3 = Season('summer', 70, [15, 35])
    season4 = Season('winter', 30, [-50, 0])

    assert season1 == season2
    assert season1 != season3
    assert season3 != season4

def test_randomTemperature():
    season1 = Season('summer', 70, [15, 35])
    season2 = Season('winter', 30, [-50, 0])

    temp1 = season1.randomTemperature(1)
    assert temp1 >= 15 and temp1 <= 35
    assert str(temp1)[::-1].find('.') == 1 # one decimal place

    temp2 = season2.randomTemperature(3)
    assert temp2 >= -50 and temp2 <= 0
    assert str(temp2)[::-1].find('.') == 3 # three decimal places
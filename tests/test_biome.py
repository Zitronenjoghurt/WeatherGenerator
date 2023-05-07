import pytest
from lemon_weather_generator.classes import Biome, Season, Seasons
from lemon_weather_generator.classes.errors import DayOutOfBiomeRange

def test_eq():
    biome1 = Biome('temperate', 'C', [{'name': 'spring', 'daytime_percentage': 50, 'temperatures': [0, 20]}])
    biome2 = Biome('temperate', 'C', [{'name': 'spring','daytime_percentage': 50, 'temperatures': [0, 20]}])
    biome3 = Biome('polar', 'C', [{'name': 'summer','daytime_percentage': 70, 'temperatures': [-10, 5]}])
    biome4 = Biome('polar', 'C', [{'name': 'winter','daytime_percentage': 30, 'temperatures': [10, 30]}])

    assert biome1 == biome2
    assert biome2 != biome3
    assert biome3 != biome4

'''
def test_season_randomTemperature():
    biome1 = Biome('temperate', 'C', [{'name': 'winter','daytime_percentage': 30, 'temperatures': [-50, 50]}])
    biome2 = Biome('scorching_hot', 'C', [{'name': 'summer','daytime_percentage': 70, 'temperatures': [50, 150]}])

    temp1 = biome1['winter'].randomTemperature()
    assert temp1 >= -50 and temp1 <= 50
    assert str(temp1)[::-1].find('.') == 2 # two decimal places

    temp2 = biome2['summer'].randomTemperature()
    assert temp2 >= 50 and temp2 <= 150
    assert str(temp2)[::-1].find('.') == 2 # two decimal places
'''

def test_getTotalAmountOfDays():
    biome1 = Biome('temperate', 'C', [{'name': 'winter', 'amount_of_days': 90}, {'name': 'spring', 'amount_of_days': 60}])
    biome2 = Biome('temperate', 'C', [{'name': 'winter', 'amount_of_days': 1}, {'name': 'spring', 'amount_of_days': 1}, {'name': 'summer', 'amount_of_days': 87}])
    biome3 = Biome('temperate', 'C', [{'name': 'winter', 'amount_of_days': 189}])

    assert biome1.getTotalAmountOfDays() == 150
    assert biome2.getTotalAmountOfDays() == 89
    assert biome3.getTotalAmountOfDays() == 189

def test_getSeasonFromDayOfYear():
    biome = Biome('temperate', 'C', [{'name': 'winter', 'amount_of_days': 90}, {'name': 'spring', 'amount_of_days': 60}])
    winter = Season(name='winter', amount_of_days=90)
    spring = Season(name='spring', amount_of_days=60)

    assert biome.getSeasonFromDayOfYear(1) == (winter, 1)
    assert biome.getSeasonFromDayOfYear(2) == (winter, 2)
    assert biome.getSeasonFromDayOfYear(30) == (winter, 30)
    assert biome.getSeasonFromDayOfYear(91) == (spring, 1)
    assert biome.getSeasonFromDayOfYear(92) == (spring, 2)
    assert biome.getSeasonFromDayOfYear(150) == (spring, 60)
    
    with pytest.raises(DayOutOfBiomeRange, match="Day '0' of biome 'temperate' is out of range 1 to 150."):
        biome.getSeasonFromDayOfYear(0)

    with pytest.raises(DayOutOfBiomeRange, match="Day '151' of biome 'temperate' is out of range 1 to 150."):
        biome.getSeasonFromDayOfYear(151)
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

def test_getTransitionSeason():
    seasons = Seasons(None, [{'name': 'spring', 'temperatures': [0, 20]}, {'name': 'summer', 'temperatures': [15, 45]}, {'name': 'autumn', 'temperatures': [5, 10]}])

    spring_half_summer = seasons['spring'].getTransitionSeason(90)

    assert spring_half_summer.temperatures.min == 7.5
    assert spring_half_summer.temperatures.max == 32.5
    assert spring_half_summer.temperatures.mean == 20
    assert spring_half_summer.temperatures.deviation == 50
    assert seasons['summer'].getTransitionSeason(45) == seasons['summer']
    assert seasons['summer'].getTransitionSeason(46) != seasons['summer']

def test_getPreviousSeason():
    seasons = Seasons(None, [{'name': 'spring', 'temperatures': [0, 20]}, {'name': 'summer', 'temperatures': [15, 45]}, {'name': 'autumn', 'temperatures': [5, 10]}])

    assert seasons['spring'].getPreviousSeason().name == 'autumn'
    assert seasons['summer'].getPreviousSeason().name == 'spring'
    assert seasons['autumn'].getPreviousSeason().name == 'summer'

def test_getNextSeason():
    seasons = Seasons(None, [{'name': 'spring', 'temperatures': [0, 20]}, {'name': 'summer', 'temperatures': [15, 45]}, {'name': 'autumn', 'temperatures': [5, 10]}])

    assert seasons['spring'].getNextSeason().name == 'summer'
    assert seasons['summer'].getNextSeason().name == 'autumn'
    assert seasons['autumn'].getNextSeason().name == 'spring'

def test_getIndexInSeasonList():
    seasons = Seasons(None, [{'name': 'spring', 'temperatures': [0, 20]}, {'name': 'summer', 'temperatures': [15, 45]}, {'name': 'autumn', 'temperatures': [5, 10]}])

    assert seasons['spring'].getIndexInSeasonList() == 0
    assert seasons['summer'].getIndexInSeasonList() == 1
    assert seasons['autumn'].getIndexInSeasonList() == 2

def test_getSunRiseHour():
    summer = Season(name='summer', daytime_percentage=70)
    winter = Season(name='winter', daytime_percentage=30)

    assert summer.getSunRiseHour() == 3.6
    assert winter.getSunRiseHour() == 8.4

def test_getSunSetHour():
    summer = Season(name='summer', daytime_percentage=70)
    winter = Season(name='winter', daytime_percentage=30)

    assert summer.getSunSetHour() == 20.4
    assert winter.getSunSetHour() == 15.6

def test_getTemperatureUnit():
    temperate = Biome('temperate', 'C', [{'name': 'spring', 'daytime_percentage': 50, 'temperatures': [0, 20]}])
    assert temperate['spring'].getTemperatureUnit() == 'C'

def test_randomTemperatureData():
    temperate = Biome('temperate', 'C', [{'name': 'spring', 'daytime_percentage': 50, 'temperatures': [0, 20]}])

    temperatureData = temperate['spring'].randomTemperatureData()
    assert temperatureData['coldest_temp'] >= temperate['spring'].temperatures.min
    assert temperatureData['warmest_temp'] <= temperate['spring'].temperatures.max
    assert temperatureData['coldest_time'] == temperate['spring'].getSunRiseHour()
    assert temperatureData['warmest_time'] == temperate['spring'].getSunSetHour()

def test_ensureMaxTemperatureDifference():
    summer = Season(name='summer', max_days_temperature_difference=5)
    winter = Season(name='winter', max_days_temperature_difference=10)

    assert summer.ensureMaxTemperatureDifference(10, 20) >= 15
    assert summer.ensureMaxTemperatureDifference(20, 10) <= 15
    assert summer.ensureMaxTemperatureDifference(10, 15) == 10
    assert summer.ensureMaxTemperatureDifference(15, 10) == 15

    assert winter.ensureMaxTemperatureDifference(10, 30) >= 20
    assert winter.ensureMaxTemperatureDifference(30, 10) <= 20
    assert winter.ensureMaxTemperatureDifference(10, 20) == 10
    assert winter.ensureMaxTemperatureDifference(20, 10) == 20
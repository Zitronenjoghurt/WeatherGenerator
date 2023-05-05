from lemon_weather_generator.classes import Season, Seasons

def test_instantiation():
    seasons = Seasons(None, [{'name': 'spring', 'temperatures': [0, 20]}])

    assert seasons['spring'].name == 'spring'
    assert seasons['spring'].temperatures.min == 0
    assert seasons['spring'].temperatures.max == 20

def test_eq():
    seasons1 = Seasons(None, [{'name': 'spring', 'temperatures': [0, 20]}])
    seasons2 = Seasons(None, [{'name': 'spring', 'temperatures': [0, 20]}])
    seasons3 = Seasons(None, [{'name': 'spring', 'temperatures': [0, 20]}, {'name': 'summer', 'temperatures': [15, 45]}])

    assert seasons1 == seasons2
    assert seasons2 != seasons3
from lemon_weather_generator.classes import Season, Seasons

def test_instantiation():
    seasons = Seasons([Season('spring', 50, [0, 20])])

    assert seasons['spring'].name == 'spring'
    assert seasons['spring'].temperatures[0] == 0
    assert seasons['spring'].temperatures[1] == 20

def test_eq():
    seasons1 = Seasons([Season('spring', 50, [0, 20])])
    seasons2 = Seasons([Season('spring', 50, [0, 20])])
    seasons3 = Seasons([Season('spring', 50, [0, 20]), Season('summer',  70, [15, 35])])

    assert seasons1 == seasons2
    assert seasons2 != seasons3
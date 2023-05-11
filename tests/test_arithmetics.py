from lemon_weather_generator.modules.arithmetics import *

def test_capBetween():
    assert capBetween(-1, 1, 150) == 149
    assert capBetween(0, 1, 150) == 150
    assert capBetween(0, 0, 150) == 0
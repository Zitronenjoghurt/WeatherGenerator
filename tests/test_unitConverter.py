from lemon_weather_generator.modules import unitConverter

def test_convertTemperature():
    assert unitConverter.convertTemperature(13.37, 'C', 'K') == 286.52
    assert unitConverter.convertTemperature(13.37, 'C', 'F') == 56.07
    assert unitConverter.convertTemperature(13.37, 'F', 'K') == 262.8
    assert unitConverter.convertTemperature(13.37, 'F', 'C') == -10.35
    assert unitConverter.convertTemperature(13.37, 'K', 'C') == -259.78
    assert unitConverter.convertTemperature(13.37, 'K', 'F') == -435.6
    assert unitConverter.convertTemperature(13.37, 'A', 'B') == 13.37

def test_convertTemperatureDifference():
    assert unitConverter.convertTemperatureDifference(10, 'C', 'C') == 10
    assert unitConverter.convertTemperatureDifference(10, 'C', 'K') == 10
    assert unitConverter.convertTemperatureDifference(10, 'C', 'F') == 18
    assert unitConverter.convertTemperatureDifference(10, 'F', 'F') == 10
    assert unitConverter.convertTemperatureDifference(10, 'F', 'C') == 5.56
    assert unitConverter.convertTemperatureDifference(10, 'F', 'K') == 5.56
    assert unitConverter.convertTemperatureDifference(10, 'K', 'K') == 10
    assert unitConverter.convertTemperatureDifference(10, 'K', 'C') == 10
    assert unitConverter.convertTemperatureDifference(10, 'K', 'F') == 18
    assert unitConverter.convertTemperatureDifference(10, 'A', 'B') == 10
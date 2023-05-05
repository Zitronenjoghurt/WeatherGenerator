from lemon_weather_generator.modules import unitConverter

def test_convertTemperature():
    assert unitConverter.convertTemperature(13.37, 'C', 'K') == 286.52
    assert unitConverter.convertTemperature(13.37, 'C', 'F') == 56.07
    assert unitConverter.convertTemperature(13.37, 'F', 'K') == 262.8
    assert unitConverter.convertTemperature(13.37, 'F', 'C') == -10.35
    assert unitConverter.convertTemperature(13.37, 'K', 'C') == -259.78
    assert unitConverter.convertTemperature(13.37, 'K', 'F') == -435.6
    assert unitConverter.convertTemperature(13.37, 'A', 'B') == 13.37
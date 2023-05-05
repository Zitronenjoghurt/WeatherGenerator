from lemon_weather_generator.modules import unitConverter

def test_convertTemperature():
    assert unitConverter.convertTemperature(13.37, 'C', 'K') == 286.5
    assert unitConverter.convertTemperature(13.37, 'C', 'F') == 56.1
    assert unitConverter.convertTemperature(13.37, 'F', 'K') == 262.8
    assert unitConverter.convertTemperature(13.37, 'F', 'C') == -10.4
    assert unitConverter.convertTemperature(13.37, 'K', 'C') == -259.8
    assert unitConverter.convertTemperature(13.37, 'K', 'F') == -435.6
    assert unitConverter.convertTemperature(13.37, 'A', 'B') == 13.4
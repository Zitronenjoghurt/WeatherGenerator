from lemon_weather_generator import loadConfigurations

def test_loadConfigurations():
    assert loadConfigurations() == {"effects": {"temperatureCloudiness": True}
}
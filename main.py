import sys

from lemon_weather_generator.classes import Configurations
from lemon_weather_generator.modules import randomizeWeather

ConfigData = Configurations.get_instance()

weather = randomizeWeather('temperate', 'winter')
print(weather)
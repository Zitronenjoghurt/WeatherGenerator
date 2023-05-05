import sys

from lemon_weather_generator.classes import Configurations
from lemon_weather_generator.modules import randomizeWeather

from matplotlib import pyplot as plt

ConfigData = Configurations.get_instance()

samples = [randomizeWeather('temperate', 'spring') for i in range(1000000)]

plt.hist(samples, bins=50)
plt.show()
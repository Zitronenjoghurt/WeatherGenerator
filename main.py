import sys

from lemon_weather_generator.modules import randomizeWeather

from matplotlib import pyplot as plt

samples = [randomizeWeather('temperate', 'spring') for i in range(1000000)]

plt.hist(samples, bins=50)
plt.show()
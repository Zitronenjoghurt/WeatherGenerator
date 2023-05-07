import sys

from lemon_weather_generator.classes.weatherData import WeatherDay

from matplotlib import pyplot as plt

samples = [WeatherDay.generateFromDayOfSeason('temperate', 'spring', 45) for i in range(1000000)]

plt.title('Spring')
plt.xlabel('Temperatures in °C')
plt.ylabel('Amount of samples')
plt.hist(samples, bins=50)
plt.show()
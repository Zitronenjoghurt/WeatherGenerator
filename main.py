import sys

from lemon_weather_generator.classes.weatherData import WeatherDay
from matplotlib import pyplot as plt

# ToDo: fix peak temperature of previous day able to be lower than low temperature of current day
biome = 'temperate'
season = 'spring'
day = 45
temperatures = WeatherDay.generateFromDayOfSeason(biome, season, day)

plt.title(f"Biome: {biome} | Season: {season} | Day: {day}")
plt.xlabel('Hours')
plt.ylabel('Temperatures in °C')
plt.plot([i for i in range(24)], temperatures)
plt.show()
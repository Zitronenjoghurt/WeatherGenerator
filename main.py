import sys

from lemon_weather_generator.classes.weatherData import WeatherDay
from matplotlib import pyplot as plt

# ToDo: add testing for new methods in season class and fix too high peak temperature differences between days
biome = 'temperate'
season = 'spring'
day = 45
temperatures = WeatherDay.generateFromDayOfSeason(biome, season, day)

plt.title(f"Biome: {biome} | Season: {season} | Day: {day}")
plt.xlabel('Hours')
plt.ylabel('Temperatures in °C')
plt.plot([i for i in range(24)], temperatures)
plt.show()
from scipy.interpolate import PchipInterpolator

from .config import Config
from .biome import Biome, Biomes
from .season import Season
from .errors import BiomeNotFound, SeasonNotFound
from ..modules.arithmetics import capBetween

class WeatherHour:
    def __init__(self, number: int, temperature: float):
        self.number = number
        self.temperature = temperature

class WeatherDay:
    def __init__(self, hours: list[WeatherHour], sunrise: str, sunset: str, season: str):
        self.hours = hours
        self.sunrise = sunrise
        self.sunset = sunset
        self.season = season

    def generateFromSeason(biome_name: str, season_name: str):
        biome = WeatherDay.validateBiome(biome_name)
        season = WeatherDay.validateSeason(biome, season_name)
        day_of_season = int(season.amount_of_days / 2) # from the middle of the season => where its the strongest

        return WeatherDay.__generate(biome, season, day_of_season)

    def generateFromDayOfYear(biome_name: str, day_of_year: int):
        biome = WeatherDay.validateBiome(biome_name)
        (season, day_of_season) = biome.getSeasonFromDayOfYear(day_of_year)

        return WeatherDay.__generate(biome, season, day_of_season)

    def generateFromDayOfSeason(biome_name: str, season_name: str, day_of_season: int):
        biome = WeatherDay.validateBiome(biome_name)
        season = WeatherDay.validateSeason(biome, season_name)

        if day_of_season < 1 or day_of_season > season.amount_of_days:
            day_of_season = capBetween(day_of_season, 1, season.amount_of_days)

        return WeatherDay.__generate(biome, season, day_of_season)

    def __generate(biome: Biome, season: Season, day_of_season: int):
        temperatures = WeatherDay.__generateTemperatures(biome, season, day_of_season)
        return temperatures

    def __generateTemperatures(biome: Biome, season: Season, day_of_season: int) -> list:
        config = Config.get_instance()
        previousDaySeason = season.getTransitionSeason(day_of_season - 1)
        currentDaySeason = season.getTransitionSeason(day_of_season)
        nextDaySeason = season.getTransitionSeason(day_of_season + 1)

        currentTempData = currentDaySeason.randomTemperatureData()
        previousTempData = previousDaySeason.randomTemperatureData(currentTempData['coldest_temp'], currentTempData['warmest_temp'])
        nextTempData = nextDaySeason.randomTemperatureData(currentTempData['coldest_temp'], currentTempData['warmest_temp'])

        hour_0 = previousTempData['warmest_time']
        temp_0 = previousTempData['warmest_temp']

        hour_1 = config.hours_per_day
        temp_1 = temp_0 - config.cooling_till_midnight * abs(temp_0 - currentTempData['coldest_temp'])

        hour_2 = config.hours_per_day + currentTempData['coldest_time']
        temp_2 = currentTempData['coldest_temp']

        hour_3 = config.hours_per_day + currentTempData['warmest_time']
        temp_3 = currentTempData['warmest_temp']

        hour_4 = config.hours_per_day * 2
        temp_4 = temp_3 - config.cooling_till_midnight * abs(temp_3 - nextTempData['coldest_temp'])

        hour_5 = nextTempData['coldest_time'] + config.hours_per_day * 2
        temp_5 = nextTempData['coldest_temp']

        hours = [hour_0, hour_1, hour_2, hour_3, hour_4, hour_5]
        temperatures = [temp_0, temp_1, temp_2, temp_3, temp_4, temp_5]

        weatherFunction = PchipInterpolator(hours, temperatures)

        temperature_list = [weatherFunction(i) for i in range(24, 48)]

        return temperature_list

        
    def validateBiome(biome_name: str) -> Biome:
        biomes = Biomes.get_instance()

        biome = biomes[biome_name]
        if biome is None:
            raise BiomeNotFound(biome_name)
        else:
            return biome
        
    def validateSeason(biome: Biome, season_name: str):
        season = biome[season_name]
        if season is None:
            raise SeasonNotFound(biome.name, season_name)
        else:
            return season
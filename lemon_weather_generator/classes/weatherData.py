from math import floor, ceil

from .config import Config
from .biome import Biome, Biomes
from .season import Season
from .errors import BiomeNotFound, SeasonNotFound, DayOutOfSeasonRange, DayOutOfBiomeRange

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
            raise DayOutOfSeasonRange(season.name, season.amount_of_days, day_of_season)

        return WeatherDay.__generate(biome, season, day_of_season)

    def __generate(biome: Biome, season: Season, day_of_season: int):
        temperatures = WeatherDay.__generateTemperatures(biome, season, day_of_season)
        return temperatures

    def __generateTemperatures(biome: Biome, season: Season, day_of_season: int) -> list:
        config = Config.get_instance()
        transitionSeason = season.getTransitionSeason(day_of_season)

        sunrise_hour = transitionSeason.getSunRiseHour()
        sunset_hour = transitionSeason.getSunSetHour()

        cooling = transitionSeason.cooling.randomize()
        warmest_temp = transitionSeason.temperatures.randomize()
        coldest_temp = warmest_temp - cooling

        heating_cooling_delay = (config.hours_per_day/2) * config.heating_cooling_offset
        coldest_time = floor(sunrise_hour + heating_cooling_delay)
        warmest_time = ceil(sunset_hour - heating_cooling_delay)
        
        heating_rate = (warmest_temp - coldest_temp) / (warmest_time - coldest_time)
        cooling_rate = heating_rate * config.cooling_rate_factor

        temperature_list = []

        # pre-sunrise cooling
        for i in range(0, coldest_time):
            temperature = round(coldest_temp - (coldest_time - i) * cooling_rate, config.decimal_digits)
            temperature_list.append(temperature)

        # heating
        for i in range(coldest_time, warmest_time):
            temperature = round(coldest_temp + (i-coldest_time) * heating_rate, config.decimal_digits)
            temperature_list.append(temperature)

        # post sunset cooling
        for i in range(warmest_time, config.hours_per_day):
            temperature = round(warmest_temp + (i-warmest_time) * cooling_rate, config.decimal_digits)
            temperature_list.append(temperature)

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
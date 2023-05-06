from .config import Config
from .biome import Biome, Biomes
from .season import Season
from .errors import BiomeNotFound, SeasonNotFound, DayOutOfSeasonRange, DayOutOfBiomeRange

class WeatherHour:
    def __init__(self, temperature: float):
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

        pass

    def __generateTemperatures(biome: Biome, season: Season, day_of_season: int):
        config = Config.get_instance()

        cooling = season.cooling.randomize()
        warmest_temp = season.temperatures.randomize()
        coldest_temp = warmest_temp - cooling

        # ToDo: finish temperature generation for hours of a day
        pass
        
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
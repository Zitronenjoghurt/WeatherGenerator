from __future__ import annotations

import random

from .config import Config
from .probability import Probability
from ..modules import unitConverter
from ..modules.valueTransition import *

class Season:
    def __init__(self, parent_seasons = None, name: str = "no_name", daytime_percentage: float = 50, temperatures: list[float]|dict = [0,20], max_days_temperature_difference: float = 5, amount_of_days: int = 90, cooling: list[float] = [0,0]):
        self.parent_seasons = parent_seasons
        self.name = name.lower()
        self.amount_of_days = amount_of_days
        self.daytime_percentage = daytime_percentage
        self.temperatures = Probability.getFromListOrDict(temperatures)
        self.cooling = Probability.getFromListOrDict(cooling)
        self.max_days_temperature_difference = max_days_temperature_difference

    def __eq__(self, other) -> bool:
        if isinstance(other, Season):
            return (self.name == other.name
                    and self.amount_of_days == other.amount_of_days
                    and self.daytime_percentage == other.daytime_percentage 
                    and self.temperatures == other.temperatures
                    and self.amount_of_days == other.amount_of_days
                    and self.cooling == other.cooling
                    and self.max_days_temperature_difference == other.max_days_temperature_difference)
        return False
    
    # The values given for a season in the config are only for the middle of a season
    # => e.g. at the beginning of spring its still a bit colder and towards the end it gets warmer, transitioning to summer
    # this function will return a season that has the proper parameters for a given day of the season
    def getTransitionSeason(self, day_of_season: int) -> Season:
        middle_of_season = int(self.amount_of_days / 2)

        targetSeason = None
        if day_of_season > middle_of_season:
            targetSeason = self.getNextSeason()
        elif day_of_season < middle_of_season:
            targetSeason = self.getPreviousSeason()
        else:
            return self
        
        progress = abs(middle_of_season - day_of_season) / (middle_of_season + targetSeason.amount_of_days/2)

        daytime_percentage = transitionValue(self.daytime_percentage, targetSeason.daytime_percentage, progress)
        amount_of_days = transitionValue(self.amount_of_days, targetSeason.amount_of_days, progress)
        temperatures = transitionValueList(self.temperatures.toList(), targetSeason.temperatures.toList(), progress)
        cooling = transitionValueList(self.cooling.toList(), targetSeason.cooling.toList(), progress)

        transitionSeason = Season(
            parent_seasons = self.parent_seasons,
            name = self.name,
            daytime_percentage = daytime_percentage,
            amount_of_days = amount_of_days,
            temperatures = temperatures,
            cooling = cooling
        )
        
        return transitionSeason

    def getPreviousSeason(self) -> Season:
        index = self.getIndexInSeasonList()
        season_list = self.parent_seasons.getSeasonList()
        
        return season_list[index - 1]

    def getNextSeason(self) -> Season:
        index = self.getIndexInSeasonList()
        season_list = self.parent_seasons.getSeasonList()

        if index + 1 >= len(season_list):
            index = -1

        return season_list[index + 1]

    def getIndexInSeasonList(self) -> int:
        return self.parent_seasons.getSeasonList().index(self)
    
    def getSunRiseHour(self) -> float:
        config = Config.get_instance()

        sunrise_hour = config.hours_per_day/2 - (config.hours_per_day*(self.daytime_percentage/100))/2
        return round(sunrise_hour, config.decimal_digits)

    def getSunSetHour(self) -> float:
        config = Config.get_instance()

        sunset_hour = config.hours_per_day/2 + (config.hours_per_day*(self.daytime_percentage/100))/2
        return round(sunset_hour, config.decimal_digits)
    
    def getTemperatureUnit(self) -> str:
        return self.parent_seasons.parent_biome.temperature_unit
    
    def randomTemperatureData(self, reference_coldest: float|None = None, reference_warmest: float|None = None) -> dict:
        config = Config.get_instance()

        warmest_temp = unitConverter.convertTemperature(self.temperatures.randomize(), self.getTemperatureUnit(), config.temperature_unit)
        cooling = unitConverter.convertTemperatureDifference(self.cooling.randomize(), self.getTemperatureUnit(), config.temperature_unit)
        coldest_temp = round(warmest_temp - cooling, config.decimal_digits)

        if reference_warmest is not None:
            warmest_temp = self.ensureMaxTemperatureDifference(warmest_temp, reference_warmest)
        if reference_coldest is not None:
            coldest_temp = self.ensureMaxTemperatureDifference(coldest_temp, reference_coldest)

        warmest_time = self.getSunSetHour()
        coldest_time = self.getSunRiseHour()

        data = {
            "coldest_temp": coldest_temp,
            "coldest_time": coldest_time,
            "warmest_temp": warmest_temp,
            "warmest_time": warmest_time
        }

        return data
    
    def ensureMaxTemperatureDifference(self, generated_temp: float|None = None, reference_temp: float|None = None) -> float:
        if reference_temp is None or generated_temp is None:
            return generated_temp
        
        tooHigh = generated_temp - reference_temp > self.max_days_temperature_difference
        tooLow = reference_temp - generated_temp > self.max_days_temperature_difference
        
        if tooHigh:
            return round(reference_temp + random.uniform(0, self.max_days_temperature_difference))
        elif tooLow:
            return round(reference_temp - random.uniform(0, self.max_days_temperature_difference))
        else:
            return generated_temp


class Seasons:
    def __init__(self, parent_biome = None, season_list: list[dict] = []):
        self.parent_biome = parent_biome
        self.season_dict = {}

        for season in season_list:
            if season['name'] not in self.season_dict:
                self.season_dict[season['name']] = Season(self, **season)

    def __eq__(self, other) -> bool:
        if isinstance(other, Seasons):
            return (self.season_dict == other.season_dict)
        return False

    def __getitem__(self, key: str) -> Season:
        return self.season_dict[key.lower()]
    
    def getSeasonList(self) -> list[Season]:
        return list(self.season_dict.values())
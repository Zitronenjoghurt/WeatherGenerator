import random

from .config import Config
from .probability import Propability
from ..modules import unitConverter

class Season:
    def __init__(self, parent_seasons = None, name: str = "no_name", daytime_percentage: float = 50, temperatures: list|dict = [0,20], amount_of_days: int = 90):
        self.parent_seasons = parent_seasons
        self.name = name.lower()
        self.amount_of_days = amount_of_days
        self.daytime_percentage = daytime_percentage

        if type(temperatures) == dict:
            self.temperatures = Propability(**temperatures)
        else:
            self.temperatures = Propability.getFromList(temperatures)

    def __eq__(self, other) -> bool:
        if isinstance(other, Season):
            return (self.name == other.name 
                    and self.amount_of_days == other.amount_of_days
                    and self.daytime_percentage == other.daytime_percentage 
                    and self.temperatures == other.temperatures)
        return False
    
    def randomTemperature(self) -> float:
        config = Config.get_instance()

        source_unit = self.parent_seasons.parent_biome.temperature_unit
        target_unit = config.temperature_unit

        temp = self.temperatures.randomize()
        return unitConverter.convertTemperature(temp, source_unit, target_unit)

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
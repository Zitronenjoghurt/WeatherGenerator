import random

from .config import Config
from .probability import Probability
from ..modules import unitConverter

class Season:
    def __init__(self, parent_seasons = None, name: str = "no_name", daytime_percentage: float = 50, temperatures: list[float]|dict = [0,20], amount_of_days: int = 90, cooling: list[float] = [0,0]):
        self.parent_seasons = parent_seasons
        self.name = name.lower()
        self.amount_of_days = amount_of_days
        self.daytime_percentage = daytime_percentage
        self.temperatures = Probability.getFromListOrDict(temperatures)
        self.cooling = Probability.getFromListOrDict(cooling)

    def __eq__(self, other) -> bool:
        if isinstance(other, Season):
            return (self.name == other.name
                    and self.amount_of_days == other.amount_of_days
                    and self.daytime_percentage == other.daytime_percentage 
                    and self.temperatures == other.temperatures
                    and self.amount_of_days == other.amount_of_days
                    and self.cooling == other.cooling)
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
    
    def getSeasonList(self) -> list[Season]:
        return list(self.season_dict.values())
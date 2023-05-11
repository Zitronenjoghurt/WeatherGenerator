import os
import json
from bisect import bisect_left
from itertools import accumulate

from .season import Season, Seasons
from ..modules.arithmetics import capBetween

config_path = os.path.join(os.path.dirname(__file__), '..', 'configurations')

biome_path = config_path + "\\biomes"
biome_files = [f for f in os.listdir(biome_path) if f.endswith('.json')]

class Biome:
    def __init__(self, name: str = "no_name", temperature_unit: str = "C", seasons: list = []):
        self.name = name.lower()
        self.temperature_unit = temperature_unit

        season_list = []
        for season in seasons:
            season_list.append(season)
        self.seasons = Seasons(self, season_list)

    def __eq__(self, other) -> bool:
        if isinstance(other, Biome):
            return (self.name == other.name and self.temperature_unit == other.temperature_unit and self.seasons == other.seasons)
        return False
    
    def __getitem__(self, season_name: str) -> Season:
        return self.seasons[season_name]
    
    def getTotalAmountOfDays(self) -> int:
        return sum(season.amount_of_days for season in self.seasons.getSeasonList())
    
    def getSeasonFromDayOfYear(self, day_of_year: int) -> tuple[Season, int]:
        biome_max_days = self.getTotalAmountOfDays()

        if day_of_year < 1 or day_of_year > biome_max_days:
            day_of_year = capBetween(day_of_year, 1, biome_max_days)
    
        cumulative_days = [0] + list(accumulate(season.amount_of_days for season in self.seasons.getSeasonList()))
    
        season_index = bisect_left(cumulative_days, day_of_year) - 1
        resulting_season = list(self.seasons.getSeasonList())[season_index]
        
        day_of_season = day_of_year - cumulative_days[season_index]

        return (resulting_season, day_of_season)    
    
class Biomes:
    __instance = None

    def __init__(self):
        self.biome_dict = {}

        for file in biome_files:
            biome_file_path = biome_path + "\\" + file
            with open(biome_file_path, 'r') as f:
                data = json.load(f)
            if data['name'] not in self.biome_dict:
                self.biome_dict[data['name']] = Biome(**data)

    def __getitem__(self, key: str) -> Biome:
        return self.biome_dict[key.lower()]
    
    def get_instance():
        if Biomes.__instance is None:
            Biomes.__instance = Biomes()
        return Biomes.__instance
from .season import Season, Seasons

class Biome:
    def __init__(self, name: str, seasons: list):
        self.name = name.lower()

        season_list = []
        for season in seasons:
            season_list.append(Season(**season))
        self.seasons = Seasons(season_list)

    def __eq__(self, other) -> bool:
        if isinstance(other, Biome):
            return (self.name == other.name and self.seasons == other.seasons)
        return False
    
    def __getitem__(self, season_name: str) -> Season:
        return self.seasons[season_name]
    
class Biomes:
    def __init__(self, biome_list: list[Biome]):
        self.biome_dict = {}

        for biome in biome_list:
            if biome.name not in self.biome_dict:
                self.biome_dict[biome.name] = biome

    def __getitem__(self, key: str) -> Biome:
        return self.biome_dict[key.lower()]
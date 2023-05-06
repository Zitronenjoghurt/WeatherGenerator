class BiomeNotFound(Exception):
    def __init__(self, biome_name: str):
        self.message = f"Biome '{biome_name}' was not found."
        super().__init__(self.message)

class SeasonNotFound(Exception):
    def __init__(self, biome_name: str, season_name: str):
        self.message = f"Season '{season_name}' not found in biome '{biome_name}'."
        super().__init__(self.message)

class DayOutOfSeasonRange(Exception):
    def __init__(self, season_name: str, season_max_days: int, season_given_days: int):
        self.message = f"Day '{season_given_days}' of season '{season_name}' is out of range 1 to {season_max_days}."
        super().__init__(self.message)

class DayOutOfBiomeRange(Exception):
    def __init__(self, biome_name: str, biome_max_days: int, biome_give_days: int):
        self.message = f"Day '{biome_give_days}' of biome '{biome_name}' is out of range 1 to {biome_max_days}."
        super().__init__(self.message)
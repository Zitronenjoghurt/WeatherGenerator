import random

class Season:
    def __init__(self, name: str = "no_name", daytime_percentage: float = 50, temperatures: list = [0,20], amount_of_days: int = 90):
        self.name = name.lower()
        self.amount_of_days = amount_of_days
        self.daytime_percentage = daytime_percentage
        self.temperatures = temperatures

    def __eq__(self, other) -> bool:
        if isinstance(other, Season):
            return (self.name == other.name 
                    and self.amount_of_days == other.amount_of_days
                    and self.daytime_percentage == other.daytime_percentage 
                    and self.temperatures == other.temperatures)
        return False
    
    def randomTemperature(self, decimal_digits: int) -> float:
        temp = random.uniform(self.temperatures[0], self.temperatures[1])
        return round(temp, decimal_digits)

class Seasons:
    def __init__(self, season_list: list[Season]):
        self.season_dict = {}

        for season in season_list:
            if season.name not in self.season_dict:
                self.season_dict[season.name] = season

    def __eq__(self, other) -> bool:
        if isinstance(other, Seasons):
            return (self.season_dict == other.season_dict)
        return False

    def __getitem__(self, key: str) -> Season:
        return self.season_dict[key.lower()]
class BiomeNotFound(Exception):
    def __init__(self, biome_name: str):
        self.message = f"Biome '{biome_name}' was not found."
        super().__init__(self.message)

class SeasonNotFound(Exception):
    def __init__(self, biome_name: str, season_name: str):
        self.message = f"Season '{season_name}' not found in biome '{biome_name}'."
        super().__init__(self.message)
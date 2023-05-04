from . import Config, Biomes

class Configurations:
    __instance = None

    def __init__(self):
        self.config = Config.get_instance()
        self.biomes = Biomes.get_instance()

    def get_instance():
        if Configurations.__instance is None:
            Configurations.__instance = Configurations()
        return Configurations.__instance
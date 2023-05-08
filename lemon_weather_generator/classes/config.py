import os
import json

config_path = os.path.join(os.path.dirname(__file__), '..', 'configurations')
class Config:
    __instance = None

    def __init__(self):
        with open(config_path + "\\config.json", 'r') as f:
            data = json.load(f)

        self.decimal_digits = data['decimal_digits']
        self.time_format = data['time_format']
        self.temperature_unit = data['temperature_unit']
        self.hours_per_day = data['hours_per_day']
        self.heating_cooling_offset = data['heating_cooling_offset']
        self.cooling_rate_factor = data['cooling_rate_factor']
        self.effects = data['effects']

    def get_instance():
        if Config.__instance is None:
            Config.__instance = Config()
        return Config.__instance
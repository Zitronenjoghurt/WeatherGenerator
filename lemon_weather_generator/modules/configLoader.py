import json
import os

config_path = os.path.join(os.path.dirname(__file__), '..', 'configurations', 'config.json')

def getConfig():
    with open(config_path, 'r') as f:
        config_dict = json.load(f)

    return config_dict
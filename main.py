import sys

from lemon_weather_generator import loadConfigurations, randomizeWeather

ConfigData = loadConfigurations()

def validateCommandArguments(args):
    del args[0]

    if (len(args) == 0):
        print("\nNo arguments given. Please read the documentation at https://github.com/Zitronenjoghurt/WeatherGenerator for more info.")
        exit()

    if (len(args) < 2):
        print("\nYou need to specify 2 arguments. Please read the documentation at https://github.com/Zitronenjoghurt/WeatherGenerator for more info.")
        exit()

    biomeName = args[0].lower()
    if (ConfigData.biomes[biomeName] is None):
        print("\nThe given biome does not exit. Check your configurations or read the documentation at https://github.com/Zitronenjoghurt/WeatherGenerator.")
        exit()

    seasonName = args[1].lower()
    if (ConfigData.biomes[biomeName][seasonName] is None):
        print("\nThe given season is not specified in the given biome. Check your configurations or read the documentation at https://github.com/Zitronenjoghurt/WeatherGenerator.")
        exit()

    return biomeName, seasonName

biomeName, seasonName = validateCommandArguments(sys.argv)

weather = randomizeWeather(biomeName, seasonName)
print(weather)
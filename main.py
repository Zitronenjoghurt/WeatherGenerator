import sys

from lemon_weather_generator import loadConfigurations, randomizeWeather

ConfigData = loadConfigurations()

def validateCommandArguments(args):
    del args[0]

    if (len(args) == 0):
        print("\nNo arguments given. Please read the documentary at https://github.com/Zitronenjoghurt/WeatherGenerator for more info.")
        exit()

    biome = args[0]
    if (ConfigData.biomes.findBiomeByName(biome) is None):
        print("\nThe given biome does not exit. Check your configurations or read the documentary at https://github.com/Zitronenjoghurt/WeatherGenerator.")
        exit()

    return biome

biome = validateCommandArguments(sys.argv)

weather = randomizeWeather(biome)
print(weather)
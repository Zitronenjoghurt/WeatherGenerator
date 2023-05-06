# WeatherGenerator (work in progress | highly unfinished)
Generates detailed random weather data for use in e.g. creative writing or roleplay while aiming to be highly customizable and easily extendable. You can either use it via command line or include the library in your own project!

## Command line
This instructions will explain how to set up WeatherGenerator for use via command line.

### Prerequisites
The things you need to have preinstalled:
- Python (3.11 or higher)
- Git

### Clone the project
In the console of your choosing run:
```
git clone https://github.com/Zitronenjoghurt/WeatherGenerator.git
```

---------------------------------------

# Configuration

## config.json
To customize general settings you can edit `/configurations/config.json`

|Property|Type|Description|Default|Values|
|---|---|---|---|---|
|`decimal_digits`|int|How many decimal places randomly generated numbers will have.|`2`||
|`temperature_unit`|str|The unit that gets used for randomly generated temperatures.|`C`|`K`= K \| `C`=°C \| `F`=°F
|`hours_per_day`|int|How many hours of weather forecast each day should have.|`24`||

## Biomes
To customize biomes you can create or edit files in `/configurations/biomes`. An example biome for reference is `temperate.json`.

|Property|Type|Description|Default|Values|
|---|---|---|---|---|
|`name`|str|The name of the biome. It's case insensitive and has to be unique.|`no_name`||
|`temperature_unit`|str|The unit of the specified seasons temperature data.|`C`|`K`= K \| `C`=°C \| `F`=°F
|`seasons`|list[Seasons]|Different seasons of the biome which each have different data to generate a realistic variation of weather data. (Look in the Seasons section for more info)|`[]`||

## Seasons
(Look in the Biomes section for reference.) Each biome has different season with different data. You can specify as many seasons as you want for every biome.

|Property|Type|Description|Default|Values|
|---|---|---|---|---|
|`name`|str|The name of the season. It's case insensitive and has to be unique.|`no_name`||
|`amount_of_days`|int|The amount of days the season will have.|`90`||
|`daytime_percentage`|float|The percentage of daylight the first day of a season has. 50 means 50% day, 50% night. 60 means 60% day, 40% night. Throughout the season the daytime_percentage will gradually shift towards that of the next season.|`50`| between 0 and 100|
|`temperatures`|list[float] or dict|You can either use a list with lowest and highest temperature or a dictionary containing the following values: min, max, mean, deviation|`[0, 20]`|`[float, float]` or `{'min': float, 'max': float, 'mean': float, 'deviation': float}`|
|`cooling`|list[float] or dict|Generates a random cooling value from the given probabilities. Cooling will determine how much cooler the coldest temperature of a day compared to the warmest temperature of a day is.|`[0,0]`|`[float, float]` or `{'min': float, 'max': float, 'mean': float, 'deviation': float}`|
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
|`temperature_unit`|str|The unit that gets used for randomly generated temperatures.|`"C"`|`"K"`= K \| `"C"`=°C \| `"F"`=°F
|`time_format`|str|Your preferred time format|`"24"`|`"12"` or `"24"`|
|`hours_per_day`|int|How many hours of weather forecast each day should have.|`24`||
|`cooling_till_midnight`|float|How much of the cooling from the current peak temperature to the lowest temperature of the next day is completed at midnight. 0.75 means that the temperature at midnight already cooled down 75% to the lowest temperature of the next day.|`0.6`|0 to 1|

## Biomes
To customize biomes you can create or edit files in `/configurations/biomes`. An example biome for reference is `temperate.json`.

|Property|Type|Description|Default|Values|
|---|---|---|---|---|
|`name`|str|The name of the biome. It's case insensitive and has to be unique.|`"no_name"`||
|`temperature_unit`|str|The unit of the specified seasons temperature data.|`"C"`|`"K"`= K \| `"C"`=°C \| `"F"`=°F
|`seasons`|list[Seasons]|Different seasons of the biome which each have different data to generate a realistic variation of weather data. (Look in the Seasons section for more info)|`[]`||

## Seasons
(Look in the Biomes section for reference.) Each biome has different season with different data. You can specify as many seasons as you want for every biome.

|Property|Type|Description|Default|Values|
|---|---|---|---|---|
|`name`|str|The name of the season. It's case insensitive and has to be unique.|`"no_name"`||
|`amount_of_days`|int|The amount of days the season will have.|`90`||
|`daytime_percentage`|float|The percentage of daylight the first day of a season has. 50 means 50% day, 50% night. 60 means 60% day, 40% night. Throughout the season the daytime_percentage will gradually shift towards that of the next season.|`50`|between 0 and 100|
|`temperatures`|list[float] or dict|For generating random max/peak temperature values for days of the season.|`[0, 20]`|`[float, float]` or `{'min': float, 'max': float, 'mean': float, 'deviation': float}`|
|`max_days_temperature_difference`|float|The maximum difference of peak and low temperatures between two days.|`5`|greater or equal 0|
|`cooling`|list[float] or dict|For generating random cooling values for days of the season. Cooling will determine how much cooler the coldest temperature of a day compared to the warmest temperature of a day is.|`[0,0]`|`[float, float]` or `{'min': float, 'max': float, 'mean': float, 'deviation': float}`|
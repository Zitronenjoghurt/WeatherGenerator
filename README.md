# WeatherGenerator (work in progress | not ready for use yet)
Generates detailed random weather data for use in e.g. creative writing or roleplay while aiming to be highly customizable and easily extendable. You can either use it via command line or include the library in your own project!

## Command line
This instructions will explain how to set up WeatherGenerator for use via command line.

### Prerequisites
The things you need to have preinstalled:
- Python (3.11 or higher)
- Git

### Clone the project
In the console of your chosing run:
```
git clone https://github.com/Zitronenjoghurt/WeatherGenerator.git
```

### Using it in command line
Head to the WeatherGenerator directory. WeatherGenerator can generate weather based on different parameters like biome and season. An example on how to use it would be:
```
python main.py temperate summer
```
This will return some weather data based on configurations you can easily edit yourself (look in the Configuration section for more info).

### General command syntax
As you have probably already noticed, the general syntax for using the weather generator is as follows (while not including the {}):
```
python main.py {biome} {season}
```

## Configuration
from lemon_weather_generator.classes.config import Config

def convertTemperature(value: float, original_unit: str, target_unit: str) -> float:
    config = Config.get_instance()
    conversion = (original_unit.capitalize(), target_unit.capitalize())

    result = value
    match conversion:
        case ('C', 'K'):
            result = value + 273.15
        case ('C', 'F'):
            result = (value * (9/5)) + 32
        case ('F', 'K'):
            result = (value - 32) * (5/9) + 273.15
        case ('F', 'C'):
            result = (value - 32) * (5/9)
        case ('K', 'C'):
            result = value - 273.15
        case ('K', 'F'):
            result = (value - 273.15) * (9/5) + 32
    
    return round(result, config.decimal_digits)
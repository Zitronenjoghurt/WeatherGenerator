from ..classes.config import Config

def hoursToTimeString(hours: float = 0, format: str = "0"):
    if format == "0":
        format = Config.get_instance().time_format
    
    hour = int(hours)
    minute = int(round(hours - hour, 2) * 60)

    if format == "12":
        am_pm = "am" if hour < 12 else "pm"
        hour = hour % 12 or 12
        return f"{hour:02d}:{minute:02d}{am_pm}"
    elif format == "24":
        if hour == 24:
            hour = 0
        return f"{hour:02d}:{minute:02d}"
    else:
        return hours
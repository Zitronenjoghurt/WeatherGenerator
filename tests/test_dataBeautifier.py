from lemon_weather_generator.modules.dataBeautifier import *

def test_hoursToTimeString():
    assert hoursToTimeString(0, "12") == "12:00am"
    assert hoursToTimeString(0, "24") == "00:00"

    assert hoursToTimeString(1, "12") == "01:00am"
    assert hoursToTimeString(1, "24") == "01:00"

    assert hoursToTimeString(5.8, "12") == "05:48am"
    assert hoursToTimeString(5.8, "24") == "05:48"

    assert hoursToTimeString(11.1, "12") == "11:06am"
    assert hoursToTimeString(11.1, "24") == "11:06"

    assert hoursToTimeString(12, "12") == "12:00pm"
    assert hoursToTimeString(12, "24") == "12:00"

    assert hoursToTimeString(13.5, "12") == "01:30pm"
    assert hoursToTimeString(13.5, "24") == "13:30"

    assert hoursToTimeString(24, "12") == "12:00pm"
    assert hoursToTimeString(24, "24") == "00:00"
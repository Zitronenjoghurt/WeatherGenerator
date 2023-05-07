from lemon_weather_generator.modules.valueTransition import *

def test_transitionValue():
    assert transitionValue(5, 10, 0) == 5
    assert transitionValue(5, 10, 0.5) == 7.5
    assert transitionValue(5, 10, 1) == 10

def test_transitionValueList():
    source = [2, 5, 10]
    target = [4, 10, 20]

    assert transitionValueList(source, target, 0) == source
    assert transitionValueList(source, target, 0.5) == [3, 7.5, 15]
    assert transitionValueList(source, target, 1) == target
def capBetween(value, min, max):
    range_size = max - min + 1
    return ((value - min) % range_size) + min
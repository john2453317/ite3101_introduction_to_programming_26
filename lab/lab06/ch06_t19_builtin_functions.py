def distance_from_zero(arg):
    if isinstance(arg, (int, float)):
        return abs(arg)
    else:
        return "Nope"

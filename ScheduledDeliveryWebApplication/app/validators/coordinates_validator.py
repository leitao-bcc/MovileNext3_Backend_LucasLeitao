

def is_valid_latitude(var):
    if type(var) != float:
        return False

    return -90 <= var <= 90


def is_valid_longitude(var):
    if type(var) != float:
        return False

    return -180 <= var <= 180

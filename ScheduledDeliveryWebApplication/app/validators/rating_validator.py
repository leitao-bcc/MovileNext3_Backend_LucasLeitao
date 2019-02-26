
def is_valid_rating(var):
    if type(var) != float:
        return False

    return 0 <= var <= 5
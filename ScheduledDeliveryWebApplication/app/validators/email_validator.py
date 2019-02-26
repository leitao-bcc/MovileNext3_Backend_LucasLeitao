from re import match


def is_valid_email(var):
    return match(r"[^@]+@[^@]+\.[^@]+", var) != None

from re import findall


def is_valid_ddd(var):
    if type(var) != int:
        return False

    return len(str(var)) == 2


def is_valid_phone_number(var):
    if not var:
        return False

    only_numbers = "".join(findall("[0-9]", var))

    return 8 <= len(only_numbers) <= 9

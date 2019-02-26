from re import findall


def is_valid_cep(var):
    if not var:
        return False

    only_numbers = "".join(findall("[0-9]", var))

    return len(only_numbers) == 8

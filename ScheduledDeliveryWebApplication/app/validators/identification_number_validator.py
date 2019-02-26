from re import findall


def is_valid_cpf(var):
    if not var:
        return False

    cpf = "".join(findall("[0-9]", var))

    if len(cpf) != 11:
        return False

    validator_string = [int(x) for x in cpf]

    cpf = validator_string[:9]

    while len(cpf) < 11:

        r = sum([(len(cpf) + 1 - i) * v for i, v in [(x, cpf[x]) for x in range(len(cpf))]]) % 11

        if r > 1:
            f = 11 - r
        else:
            f = 0
        cpf.append(f)

    return cpf == validator_string


def is_valid_cnpj(var):
    if not var:
        return False

    cnpj = "".join(findall("[0-9]", var))

    if len(cnpj) != 11:
        return False

    list_validation_one = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    list_validation_two = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    checker = cnpj[-2:]

    sum = 0
    id = 0
    for number in cnpj:
        try:
            list_validation_one[id]
        except:
            break
        sum += int(number) * int(list_validation_one[id])
        id += 1

    sum = sum % 11
    if sum < 2:
        digit_one = 0
    else:
        digit_one = 11 - sum

    digit_one = str(digit_one)

    sum = 0
    id = 0
    for number in cnpj:
        try:
            list_validation_two[id]
        except:
            break

        sum += int(number) * int(list_validation_two[id])
        id += 1

    sum = sum % 11
    if sum < 2:
        digit_two = 0
    else:
        digit_two = 11 - sum

    digit_two = str(digit_two)

    return checker == digit_one + digit_two

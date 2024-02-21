def valid_digit(cpf, digit_to_validate):
    if digit_to_validate != 10 and digit_to_validate != 11:
        return

    aux = digit_to_validate

    numbers_to_sum = []

    while aux >= 2:
        numbers_to_sum.append(aux * cpf[digit_to_validate - aux])
        aux -= 1

    sum = 0

    for i in numbers_to_sum:
        sum += i

    if sum % 11 < 2:
        final_number = 0
    else:
        final_number = 11 - sum % 11

    return final_number == cpf[digit_to_validate - 1]


def cpf_validator(cpf):
    if len(cpf) != 11:
        return False

    # The third statement is to check if all elements in cpf are equal to each other
    if valid_digit(cpf, 10) and valid_digit(cpf, 11) and not (cpf and all(cpf[0] == elem for elem in cpf)):
        return True
    else:
        return False


def format_cpf_pattern(cpf):
    return ''.join(str(digit) for digit in cpf[0:3]) + "." \
        + ''.join(str(digit) for digit in cpf[3:6]) + "." \
        + ''.join(str(digit) for digit in cpf[6:9]) + "-" \
        + ''.join(str(digit) for digit in cpf[9:11])

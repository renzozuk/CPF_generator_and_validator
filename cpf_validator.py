import re
from util.cpf_helper import cpf_validator

user_input = input('Digite o CPF: ')

cpf = re.sub('[^0-9]', '', user_input)

is_cpf_valid = cpf_validator([int(digit) for digit in cpf])
print(is_cpf_valid)

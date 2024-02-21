import random
from util.cpf_helper import cpf_validator, format_cpf_pattern
from util.instructions_helper import print_fiscal_region_instructions


def common_generate(cpf):
    cpf.clear()

    for i in range(11):
        cpf.append(random.randint(0, 9))

    return cpf


def generate_by_fiscal_region(cpf, fiscal_region: int):
    cpf.clear()

    cpf = common_generate(cpf)

    cpf[8] = fiscal_region

    return cpf


cpf = []

choice = ''

while choice.lower() != 's' and choice.lower() != 'n':
    choice = input("Você quer gerar um CPF de algum estado específico? (s/n): ")

if choice.lower() == 's':
    print_fiscal_region_instructions()

    fiscal_region = -1

    while fiscal_region < 0 or fiscal_region > 9:
        try:
            fiscal_region = int(input("Sua escolha: "))
        except ValueError:
            print("Apenas números inteiros são suportados. Por favor, escolha novamente.")
            fiscal_region = -1

    while not cpf_validator(cpf):
        generate_by_fiscal_region(cpf, fiscal_region)

else:
    while not cpf_validator(cpf):
        common_generate(cpf)


cpf_str = format_cpf_pattern(cpf)

print(f"\nCPF gerado: {cpf_str}")

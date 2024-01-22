import random
from util.cpf_helper import cpf_validator


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
    print("\nRegiões fiscais:", )
    print("1 - DF, GO, MT, MS e TO;")
    print("2 - AC, AP, AM, PA, RO e RR;")
    print("3 - CE, MA e PI;")
    print("4 - AL, PB, PE e RN;")
    print("5 - BA e SE;")
    print("6 - MG;")
    print("7 - ES e RJ;")
    print("8 - SP;")
    print("9 - PR e SC;")
    print("0 - RS.", end="\n\n")

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


cpf_str = ''.join(str(digit) for digit in cpf[0:3]) + "." \
        + ''.join(str(digit) for digit in cpf[3:6]) + "." \
        + ''.join(str(digit) for digit in cpf[6:9]) + "-" \
        + ''.join(str(digit) for digit in cpf[9:11]) \

print(f"\nCPF gerado: {cpf_str}")

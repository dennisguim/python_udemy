import re

cpf = input("Insira o seu CPF: ")

cpf_validado = re.sub(
    r'[^0-9]',
    '',
    cpf
)

print(f'o cpf é: {cpf_validado}')
#calcular o segundo dígito do CPF
cpf = '53324285704'
cpf_nove = cpf[:9]
cpf_dez = cpf[:10]
multiplicador_1 = 10
multiplicador_2 = 11

calculo_1 = 0
calculo_2 = 0 

for digito_1 in cpf_nove:
    calculo_1 += int(digito_1) * multiplicador_1
    multiplicador_1 -= 1

for digito_2 in cpf_dez:
    calculo_2 += int(digito_2) * multiplicador_2
    multiplicador_2 -= 1

digito_1 = calculo_1 * 10 % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

digito_2 = calculo_2 * 10 % 11
digito_2 = digito_2 if digito_2 <= 9  else 0


print(digito_1)
print(digito_2)



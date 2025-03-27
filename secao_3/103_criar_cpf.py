import random

cpf_sem_digito = ''

calculo_1 = 0
calculo_2 = 0

multiplicador_1 = 10
multiplicador_2 = 11


for i in range(9):
    cpf_sem_digito += str(random.randint(0, 9))

for digito_1 in cpf_sem_digito:
    calculo_1 += int(digito_1) * multiplicador_1
    multiplicador_1 -= 1

calculo_1 = calculo_1 * 10 % 11
calculo_1 = calculo_1 if calculo_1 <= 9 else 0

for digito_2 in cpf_sem_digito + str(calculo_1):
    calculo_2 += int(digito_2) * multiplicador_2
    multiplicador_2 -= 1

calculo_2 = calculo_2 * 10 % 11
calculo_2 = calculo_2 if calculo_2 <=9 else 0

cpf_completo = cpf_sem_digito + str(calculo_1) + str(calculo_2)

print(cpf_completo)

cpf_novo = ''

for digitos in cpf_completo:
    if len(cpf_novo) >= 2 and len(cpf_novo) < 3:
        cpf_novo += digitos + "."
    elif len(cpf_novo) >= 6 and len(cpf_novo) < 7:
        cpf_novo += digitos + "."
    elif len(cpf_novo) >= 10 and len(cpf_novo) < 11:
        cpf_novo += digitos + "-"
    else:
        cpf_novo += digitos
 
print (f'CPF gerado: {cpf_novo}')
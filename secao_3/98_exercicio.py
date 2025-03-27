cpf = "53324285704"
cpf_corte = cpf[:9]
multiplicador = 10
digitos = []
somados = 0

for digito in cpf_corte:
    passo1 = int(digito) * multiplicador
    digitos.append(passo1)
    multiplicador -= 1

for digito_2 in digitos:
    somados += int(digito_2)

passo3 = somados * 10
passo4 = passo3 % 11

if passo4 <= 9:
    passo4 = passo4
else:
    passo4 = 0


print(digitos)
print(somados)
print(passo4)


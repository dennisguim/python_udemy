cpf = "53324285704"
cpf_nove = cpf[:9]
multiplicador = 10
""" digitos = [] """
somados = 0

for digito in cpf_nove:
    somados += int(digito) * multiplicador
    multiplicador -= 1

digito = (somados*10) % 11
digito = digito if digito <=9 else 0

print(digito)
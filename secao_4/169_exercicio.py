# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

municipios = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']
municipio = []
estado = []
municipio_estado = []
contador = len(municipios)
i = 0

while contador > 0:
    for municipio in municipios:
        juntos = municipio, estados[i]
        municipio_estado.append(juntos)
        contador -= 1
        i += 1

print(municipio_estado)
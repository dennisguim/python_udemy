""" lista = ["dennis", "breno", "thamires"]
lista_1 = []
item = input("digite: ")

for nomes in enumerate(lista):
    lista_1.append(nomes)

print(lista_1)

print(lista_1[1])

print(lista.index("dennis"))
 """
comando = input('Você deseja [i]ncluir, [r]emover ou [m]ostrar a lista? ')
comando = comando.lower()
print(comando)
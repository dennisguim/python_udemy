lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]

print(lista_soma)

# a solução do professor foi praticamente a mesma que a minha, porém ele foi mais conciso. 
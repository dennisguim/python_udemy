# o pyhton ja possui uma forma de unir listas: o zip

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zip(l1, l2)) # ele retorna a posição do iterador na memória. Para pegar os valores use list().

print(list(zip(l1, l2)))
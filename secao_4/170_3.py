# Agora, para pegar a maior lista como referencia tem que importar o itertools e o zip_longest

from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zip(l1, l2)) # ele retorna a posição do iterador na memória. Para pegar os valores use list().

print(list(zip_longest(l1, l2)))
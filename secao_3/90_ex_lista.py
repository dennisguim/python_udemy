import os

lista_compras = []
""" indice_lista = [] """

while True:
    """ for item in lista_compras:
        indice_lista.append(item) """

    comando = input('Você deseja [i]ncluir, [r]emover ou [m]ostrar a lista? ')
    comando = comando.lower()
    os.system("clear")
    if comando == "i":
        incluir = input("Digite o item que você deseja incluir na lista: ")
        lista_compras.append(incluir.lower())
    elif comando == "r":
        remover = input("Digite o item que você deseja remover da lista: ")
        remover = remover.lower()
        if remover in lista_compras:
            remover_item = lista_compras.index(remover)
            lista_compras.pop(remover_item)
        else:
            print(f"{remover} não está na lista!")
            print(lista_compras)
    elif comando == "m":
        print(lista_compras)
    elif comando == "sair":
        break

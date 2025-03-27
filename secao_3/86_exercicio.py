lista = ["maria", "helena", "luiz", "dennis"]
indice = 0

while indice < len(lista):
    for nome in lista:
        print(f"{indice} {nome}")
        indice += 1
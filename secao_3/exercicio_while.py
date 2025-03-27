nome = "Dennis Guimaraes"


contador = 0
novo_nome = ""

while contador < len(nome):
    
    letra = f"*{nome[contador]}"
    contador += 1
    
    if contador == 7:
        letra = f" *{nome[contador]}"
        contador += 1

    novo_nome = novo_nome + letra
print(novo_nome)
    

    

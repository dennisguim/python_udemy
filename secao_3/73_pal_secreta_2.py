import os

palavra_secreta = "dennis"
letra_acertada = ""
tentativas = 0

while True:
    letra_dig = input("Digite uma letra: ")
    tentativas += 1

    if len(letra_dig) > 1:
        print("Digite apenas uma letra.")
        continue
    
    if letra_dig in palavra_secreta:
        letra_acertada += letra_dig
        
    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "-"
    
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system("clear")
        print("voce ganhou!")
        print(tentativas)
        letra_acertada = ""
        tentativas = 0

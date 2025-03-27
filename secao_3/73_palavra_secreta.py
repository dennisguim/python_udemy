secreta = "dennis"
acertos = ""
bloqueado = ""




while len(acertos) < len(secreta):
    tentativa = input("Digite uma letra: ")
    if tentativa in secreta:
        acertos = acertos + tentativa
        """ for letra in secreta:
            bloqueado = bloqueado + bloqueado[letra]
            print(bloqueado) """
    else:
        print(f'{tentativa} não está na palavra secreta.')
"""         acertos = acertos
 """
for letra in secreta:
    if secreta[0] == acertos[0]:
        bloqueado = bloqueado + letra
    elif secreta[1] == acertos[1]:
        bloqueado = bloqueado + letra
    elif secreta[2] == acertos[2]:
        bloqueado = bloqueado + letra
    elif secreta[3] == acertos[3]:
        bloqueado = bloqueado + letra
    elif secreta[4] == acertos[4]:
        bloqueado = bloqueado + letra
    elif secreta[5] == acertos[5]:
        bloqueado = bloqueado + letra
    elif secreta[6] == acertos[6]:
        bloqueado = bloqueado + letra
    else:
        letra = f"-"
        bloqueado = bloqueado + letra
    
"""     print(acertos) """
print(bloqueado)

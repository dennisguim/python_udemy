#resolução do duplicar, triplicar e quadruplicar

def multiplicador(i):
    def calculo(n):
        return i * n
    return calculo


duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)


print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

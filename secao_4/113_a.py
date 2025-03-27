# Multiplicação de argumentos

def calculo_1(*args):
    total_1 = 1

    for i in args:
       total_1 *= i
      
    return total_1
    
       
print(calculo_1(1, 2, 3, 4, 5))
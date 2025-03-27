# Função par ou ímpar

def par_impar(x):
    n = x % 2 == 0

    if n:
        return "é par" 
    return "é impar"   # return não precisa de else. Ele vai retornar o valor se for True e o outro valor se for False.
   
    
    
print(par_impar(3))
perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',  
    },
    {
        'Pergunta': 'Quanto é 5 x 5?',
        'Opções': ['15', '25', '30', '35'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10 % 2:',
        'Opções': ['4', '7', '3', '5'],
        'Resposta': '5',
    }
]

qtd_dict = len(perguntas)
repeticoes = qtd_dict
contador = 0
i = 0
n = 0

while repeticoes != 0:
    lista_chaves = list(perguntas[i].keys())
    qtd_opcoes = len(perguntas[i]['Opções'])
    lista1 = list(perguntas[i]['Opções'])
    opcoes = qtd_opcoes - qtd_opcoes
    
    print("\n",
        perguntas[i]['Pergunta'],'\n','\n',
        lista_chaves[1], '\n',
        '0)', lista1[0], '\n',
        '1)', lista1[1], '\n',
        '2)', lista1[2], '\n',
        '3)', lista1[3], '\n',
          )

    resp = int(input('Escolha uma opção: '))
    resp_lista = lista1[resp]
    
    
    #print(resp)
    #print(perguntas[i]['Resposta'])

    print("\n" "Resposta errada!" if resp_lista != perguntas[i]['Resposta'] else "\n" "Correto")

    contagem = contador + 1 
    
    contagem if resp_lista == perguntas[i]['Resposta'] else ...

    i += 1
    repeticoes -= 1

    


else:
    print(f'Você acertou {contagem} de {len(perguntas)} questões')
    print('Terminou')

    """ lista_chaves = list(perguntas[1].keys())
    qtd_opcoes = len(perguntas[1]['Opções'])
    lista1 = list(perguntas[1]['Opções'])1

    print("\n",
        perguntas[1]['Pergunta'],'\n','\n',
        lista_chaves[1], '\n',
        '0)', lista1[0], '\n',
        '1)', lista1[1], '\n',
        '2)', lista1[2], '\n',
        '3)', lista1[3], '\n',
          )

    resp = input('Escolha uma opção: ') 

    print("\n" "Resposta errada!" if resp != '1'  else "Correto") """
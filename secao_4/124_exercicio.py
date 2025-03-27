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
        'Reposta': '5',
    }
]

while True:
    lista_chaves = list(perguntas[0].keys())
    print(perguntas[0]['Pergunta'],'\n', '\n',
          lista_chaves[1]
          )



    resp = input('Escolha uma opção: ')
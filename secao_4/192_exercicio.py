# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']



def adicionar(tarefa):
    tarefas.append(tarefa)
    return tarefas

tarefas = []
recall = ""
while True:
    
    questionamento = input("Digite a tarefa ou desfazer ou refazer: ")
    ...
    if questionamento.lower() == 'sair':
        print(*tarefas, sep='\n')
        break

    elif questionamento.lower() == "desfazer":
        recall = tarefas.pop(-1)
        print(*tarefas, sep='\n')
        
    elif questionamento.lower() == "refazer":
        tarefas.append(recall)
        print(*tarefas, sep='\n')

    elif questionamento.lower() != "desfazer" or questionamento.lower() != "refazer":
        tarefas = adicionar(questionamento)
        print(*tarefas, sep='\n')

    elif questionamento.lower() == 'clear':
        tarefas.clear()



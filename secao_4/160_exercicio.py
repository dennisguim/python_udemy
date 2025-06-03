# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)


novos_produtos = []

for produto in produtos:
    novo_preco = produto['preco'] * 1.1
    produto['preco'] = round(novo_preco, 2)
    novos_produtos.append(produto)

#print(novos_produtos)

produtos_preco_decrescente = sorted(novos_produtos, key=lambda produto: produto['preco'], reverse=True)

#print(produtos_preco_decrescente)

produtos_preco_crescente = sorted(novos_produtos, key=lambda produto: produto['preco'])

#print(produtos_preco_crescente)

produtos_nome_crescente = sorted(novos_produtos, key=lambda produto: produto['nome'])

produtos_nome_decrescente = sorted(novos_produtos, key=lambda produto: produto['nome'], reverse=True)

#print(produtos_nome_crescente)
print(produtos_nome_decrescente)

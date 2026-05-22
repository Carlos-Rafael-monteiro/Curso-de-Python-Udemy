# List comprehension em Python
#List comprehension é uma forma rápida para criar listas
#a partir de iteráveis.
#print(list(range(10)))

import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


lista = []
for numero in range(10):
    lista. append(numero)
#print(lista)
#print()

lista = [numero for numero in range(10)]
#print(lista)

#print()

lista = [
    numero * 2
    for numero in range(10)
]
#print(lista)
#print()

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preço': 20,},
    {'nome': 'p2', 'preço': 10,},
    {'nome': 'p3', 'preço': 30,},    
]


novos_produtos = [
    {'nome': produto['nome'], 'preço': produto['preço']}
    for produto in produtos
]

#print(novos_produtos)
print(*novos_produtos, sep='\n')
print()

novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.05}
    if produto ['preço'] > 20 else {**produto}
    for produto in produtos
    if produto ['preço'] >= 20 
]

#print(novos_produtos)
#print(*novos_produtos, sep='\n')
p(novos_produtos)
lista = [n for n in range(10) if n < 5]
p(lista)
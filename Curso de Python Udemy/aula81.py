# Fução lambda em Python
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

"""lista = [4, 32, 1, 34, 5, 6, 6, 21,]
lista.sort(reverse=True)
sorted(lista)
lista.sort()
print(lista)"""

lista = [
    {'nome': 'Rafael', 'sobrenome': 'Monteiro'},
    {'nome': 'Gercila', 'sobrenome': 'Silva'},
    {'nome': 'Nicolly', 'sobrenome': 'Silva'},
    {'nome': 'Clara', 'sobrenome': 'Monteiro'},
    {'nome': 'Aline', 'sobrenome': 'Souza'}
]

'''def ordena(item):
    return item['nome']


lista.sort(key=ordena)

for item in lista:
    print(item)

print()


lista.sort(key=lambda item: item['sobrenome'])

for c in lista:
    print(c)'''

def exibir(lista):
    for item in lista:
        print(item)

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
print()
exibir(l2)
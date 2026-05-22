# Exercício - Unir listas
#Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas 
#listas na ordem.
# Use todos os valores do menor lista.
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ,]
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
'''def zipper(Lista1, Lista2):
    intervalo_maximo = min(len(Lista1), len(Lista2))
    return[
        (Lista1[i], Lista2[i]) for i in range(intervalo_maximo)
    ]


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(l1, l2))'''
from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2)))
print()
print(list(zip_longest(l1, l2, fillvalue='Sem Cidade')))


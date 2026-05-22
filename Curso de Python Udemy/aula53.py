'''
enumerate - enumera iteráveis (indices e valores)
'''
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

#lista_enumerada = list(enumerate(lista))
#print(next(lista_enumerada))  # imprime o primeiro elemento enumerado

for indice, valor in enumerate(lista):
    # o loop for percorre cada elemento enumerado da lista
    print(indice,'-', valor)  # imprime o índice e o valor de cada elemento enumerado

#print(lista_enumerada)  # imprime a lista enumerada completa
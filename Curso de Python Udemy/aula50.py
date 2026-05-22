'''
Exeercicio 
exiba os índices da lista
0 Maria
1 Helena
2 Luiz
'''

lista = ['Maria', 'Helena', 'Luiz']
#for indice, nome in enumerate(lista):
#    print(indice,'-', nome)

indices = range(len(lista))
for indice in indices:
    print(indice, '-', lista[indice])
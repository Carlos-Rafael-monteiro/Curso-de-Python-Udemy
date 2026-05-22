'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

'''
lista_a = [1, 2, 3]
print(lista_a)
lista_b = [4, 5, 6]
print(lista_b)
lista_c = lista_a + lista_b
print(lista_c)
lista_a.extend(lista_b)
print(lista_a)

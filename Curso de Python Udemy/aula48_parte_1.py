'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update Delete

'''
#.........01234
#........-54321
string = 'ABCDE' # 5 caracteres (len)

#print(bool([])) # falsy
#print(lista,type(lista))

lista = [123, True, 'Luiz Otávio', 1.2, []]
print(lista)
lista[-3] = 'Maria' # alterando o valor
print(lista)
print(lista[2], type(lista[2]))
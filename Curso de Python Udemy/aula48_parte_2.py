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
lista = [10, 20, 30, 40]
print(lista)
# alterando valor indice 2
lista[2] = 300
print(lista)
# deletando valor indice 3
del lista[3]
print(lista)
# adicionando valor no final da lista
lista.append(49)
print(lista)
# deletando o último valor da lista
lista.pop()
print(lista)
# adicionando valor no final da lista
lista.append(50)
print(lista)
#criando varialvel com ultimo valor deletado da lista
ultimo_valor = lista.pop()
print(lista, 'Removido', ultimo_valor)
# remover um indice da lista com o pop
lista.pop(2)
print(lista)
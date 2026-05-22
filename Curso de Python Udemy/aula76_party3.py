# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iteráveil com as chaves
# values - itarável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - apaga um item com a chave especificada (del)
# popitem - apaga o último item adicionado
# update - atualiza um dicionário com outro
import copy

pessoa = {
    'nome': 'Carlos Rafael',
    'sobrenome': 'Monteiro',
    'idade': 38,
    'l1': [0,1,2]
}

pessoa2 = copy.deepcopy(pessoa)

pessoa2['nome'] = 'Gercila'

pessoa2['l1'][1] = 9999

print(pessoa)
print()
print(pessoa2)

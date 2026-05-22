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

pessoa = {
    'nome': 'Carlos Rafael',
    'sobrenome': 'Monteiro',
}

pessoa.setdefault('idade', 38)
print(pessoa['idade'])
print()
print(len(pessoa))
print()
print(tuple(pessoa.keys()))
print()
print(list(pessoa.keys()))
print()
print(pessoa.keys())
print()
print(pessoa.values())
print()
print(pessoa.items())
print()
for chave in pessoa:
    print(chave)
print()
for valor in pessoa.values():
    print(valor)
print()
for item in pessoa.items():
    print(item)
print()
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')

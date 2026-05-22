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

p1 = {
    'nome': 'Carlos Rafael',
    'sobrenome': 'Monteiro',   
}
'''nome = p1.pop('nome')
print(p1.get('nome'))
print(nome)
print(p1)
ultima_chave = p1.popitem()
print(ultima_chave)

print(p1)
p1.update({
    'nome': 'novo valor',
    'idade': 38
})'''
p1.update(nome= 'Gercila', idade= 34)
print(p1)

tupla = ('nome', 'Clara'), ('idade', 12)
p1.update(tupla)
print(p1)

lista = [['nome', 'Nicolly'], ['idade', 8]]
p1.update(lista)
print(p1)


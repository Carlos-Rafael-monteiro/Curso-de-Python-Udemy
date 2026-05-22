# Dicionaty Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}
for chave, valor in produto.items():
    print(chave,':', valor)


dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()

}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]

lt = {
    chave: valor
    for chave, valor in lista
}

print(lt)
print(dc)

s1 = {i for i in range(10)}
print(s1)
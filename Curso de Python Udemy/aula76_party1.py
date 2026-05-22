# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Carlos Rafael'
pessoa['sobrenome'] = 'Monteiro'



print(pessoa[chave])

pessoa[chave] = 'Maria'

#del pessoa['sobrenome']

print(pessoa['nome'])

print(pessoa.get('sobrenome', None))
print()
print(pessoa.get('sobrenome', 'Não existe'))
print()
if pessoa.get('sobrenome') is None:
    print('Não Existi')
else:
    print(pessoa['sobrenome'])
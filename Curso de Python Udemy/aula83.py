# Empacotamento e desempacotamento de dicionários

'''a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

a, b = pessoa.values()
print(a, b)
print()

a, b = pessoa.items()
print(a, b)

print()

(a1, a2), (b1, b2) = pessoa.items()
print(f'{a1}: {a2}')
print(b1, b2)

print()

a, b = pessoa

print (a, b)

print()

for valor in pessoa.items():
    print(valor)

print()

for chave, valor in pessoa.items():
    print(chave, valor)'''

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

print()

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args )
    #print(kwargs)
    for chave, valor in kwargs.items():
        print(chave, valor)


#mostro_argumentos_nomeados(1, 2, nome='Joana', qlqr=1234)
#print()
#mostro_argumentos_nomeados(**pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
configurações = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configurações)
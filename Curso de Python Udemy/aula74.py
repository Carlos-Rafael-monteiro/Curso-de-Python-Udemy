'''
Closure e funções que retornam outras funções
'''

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
fala_boa_noite = criar_saudacao('Bom noite')

print(falar_bom_dia('Rafael'))
print(fala_boa_noite('Clara'))

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(fala_boa_noite(nome))

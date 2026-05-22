'''
Operações ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
'''
#condicao = 10 == 11
#variavel = 'valor' if condicao else 'outro valor'
#print(variavel)

digito = 9
#novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito #invertido
print(novo_digito)
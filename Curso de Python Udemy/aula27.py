"""

Fatiamento de strings
 012345678
 Olá Mundo
-987654321
fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de caracteres da string
"""

variavel = 'Olá Mundo'
print(variavel[4:8])
print(variavel[::2])
print(len(variavel))
print(variavel[0:len(variavel):2])
print(variavel[::-1])
print(variavel[-1:-10:-1])
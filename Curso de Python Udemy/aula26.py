"""

Formatação básica de strings
s - string
d - inteiro
f - float
.<número de dígito>f
x ou X - hexadecimal
(caractere) (><^) (quantidade)
> - esquerta
< - direita
^ - centro
= - Força o número a aparecer antes do zeros
sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r ou !s ou !a ___repr___, ___str___, ___ascii___

"""
variavel = 'abc'
print(f'{variavel}')
print(f'{variavel:>10}')
print(f'{variavel:<10}')
print(f'{variavel:^10}')
print(f'{variavel:-^10}')
print(f'{1000.487364855852:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')
print(f'{variavel!s}')
print(f'{variavel!a}')
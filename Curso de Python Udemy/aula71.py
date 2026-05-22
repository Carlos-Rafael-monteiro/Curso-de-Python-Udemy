'''
args - argumentos não nomeados
* - *args (empacotamento e desempacotamento)
'''

# Lembre-se de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


#def soma(x, y):
#    return x+y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(soma(1, 2, 3, 4, 5, 6))
soma1 = soma(1, 2, 3)
print(soma1)
soma2 = soma(4, 5, 6)
print(soma2)
soma3 = soma(7, 8, 9, 10)
print(soma3)
print(sum((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
print(sum(numeros))
soma4 = soma(*numeros)
print(soma4)

# Exercicios com funções

#Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def multiplicação(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

conta1 = multiplicação(1, 2, 3, 4, 5)
print(conta1)
conta2 = multiplicação(10, 20, 30, 40, 50)
print(conta2)
conta3 = multiplicação(10, 10)
print(conta3)

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'
     
    
print(par_impar(10))
print(par_impar(11))
    
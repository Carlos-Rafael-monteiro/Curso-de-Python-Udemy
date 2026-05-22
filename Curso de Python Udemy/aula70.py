'''
REtorno de valores das funções (return)
'''
def soma(x, y):
    if x > 10:
        return 10, 20
    soma = x + y
    return soma

soma1 = soma(2, 3)
soma2 = soma(10, 20)
print(soma1 + soma2)
print(soma(11, 55))
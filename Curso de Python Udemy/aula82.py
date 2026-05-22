def executa(funcao, *args):
    return funcao(*args)


def soma(x , y):
    return x + y


print(executa(lambda x, y: x + y, 2, 3))
print()
print(executa(soma, 2, 4))
print()
print(soma(4, 4))
print()
print(executa(lambda *args: sum(args), 1, 2, 3, 4, ))


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = executa(lambda m: lambda n: n * m, 2)

print(duplica(2))
print()
#print(executa(lambda m: lambda n: n * m, 6))

print()

print('erro')

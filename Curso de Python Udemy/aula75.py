# Exercícios
#Crie funções que duplicam, triplicam e quadriplicam
# o número recebido como parâmetro

""" def dublicar(numero):
    return numero * 2


def triplicar(numero):
    return numero * 3


def quadruplicar(numero):
    return numero * 4


dobrar = dublicar(2)
print(dobrar)

triplo = triplicar(2)
print(triplo)

quadru = quadruplicar(2)
print(quadru) """

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return  numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

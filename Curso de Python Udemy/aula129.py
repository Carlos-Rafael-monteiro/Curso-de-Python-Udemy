# @statcmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da 
# classe, mas não tem acesso ao selfie nem ao cls.
# Em resumo, são funções que existem dentro da sua classe, mas não tem acesso a nada da classe.

class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('Sou uma função que está dentro da classe, mas não tenho acesso a nada da classe.')
        print(args, kwargs)


def funcao(*args, **kwargs):
    print('Sou uma função que está fora da classe.')
    print(args, kwargs)


c1 = Classe()
c1.funcao_que_esta_na_classe(1, 2, 3)
funcao(1, 2, 3)
Classe.funcao_que_esta_na_classe(nomeado=1)
funcao(nomeado=1)
# Exercício - Salve sua classe em JSON
# Salve os dadds da sua classe em JSON
# e depois crie novamente as instâncias 
# da classe com os dados salvos
# Faça em aruqivos separados.
import json
CAMINHO_ARQUIVO = 'Aula127.json'


class Pessoa:
    def __init__(self, nome, idade):
       self.nome = nome
       self.idade = idade


p1 = Pessoa('Luiz', 29)
p2 = Pessoa('Maria', 25)
p3 = Pessoa('João', 32)
p4 = Pessoa('José', 45)
bd = [vars(p1), p2.__dict__, vars(p3), vars(p4)]  # vars() ou __dict__ retorna um dicionário com os atributos do objeto


def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    fazer_dump()
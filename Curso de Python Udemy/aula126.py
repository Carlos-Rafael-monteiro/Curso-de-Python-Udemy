# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
dados = {'nome': 'Rafael', 'idade': 39}
p1 = Pessoa('João', 35)
p2 = Pessoa(**dados)

print(p1.__dict__)
print(vars(p1))
print()
print(vars(p2))
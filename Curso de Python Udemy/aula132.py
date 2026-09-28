# @property + @setter - getter e setter no modo pythonico
# - como getter
# - p/ evitar quebrar c´digo cliente
# - p/ hobilitar setter 
# - p/ executar açções ao obter um atributo
# Atributos que cameçar com um ou dois underlines são considerados privados, e não devem ser acessados diretamente fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
        self._cor = cor  # atributo privado
        self._cor_tampa = None  # atributo privado

    @property
    def cor(self):
        print('PROPERTY')
        return self._cor

    @cor.setter
    def cor(self, valor):
        print('Estou no setter', valor)
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


def mostrar_cor(caneta):
    print(caneta.cor)     # chama o método cor() e não o atributo cor_tinta


caneta = Caneta('azul')
caneta.cor = 'Rosa'  # chama o método cor() e não o atributo cor_tinta
caneta.cor_tampa = 'Preta'  # chama o método cor() e não o atributo cor_tinta
# getter -> obter valor
print(caneta.cor)  # chama o método cor() e não o atributo cor_tinta
print(caneta.cor_tampa)  # chama o método cor() e não o atributo cor_tinta
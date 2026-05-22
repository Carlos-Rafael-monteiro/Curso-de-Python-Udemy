# Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas 
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __mais__ por padrão
# O python conhece todos os módulos e pacotes presentes
# no caminhos de sys.path

import aula97_m
from aula97_m import soma1, variavel_modulo

#print('Este módulo se chama', __name__)
print(aula97_m.variavel_modulo)
print(aula97_m.soma1(2, 3))
print(variavel_modulo)
print(soma1(2, 3))

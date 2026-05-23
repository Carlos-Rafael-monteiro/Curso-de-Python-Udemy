# map - para mapear dados
from functools import partial
from types import GeneratorType

def print_iter(iterador):
    print(*list(iterador), sep='\nd')
    print()


produtos = [
    {'nome': 'Produto 5', 'preço': 10.00},
    {'nome': 'Produto 1', 'preço': 22.32},
    {'nome': 'Produto 3', 'preço': 10.11},
    {'nome': 'Produto 2', 'preço': 105.87},
    {'nome': 'Produto 4', 'preço': 69.90},   
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


aumenta_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)



'''novos_produtos = [
    {**p, 'preço': aumenta_dez_porcento(p['preço'])}
    for produto in produtos
]'''
def muda_preco_de_produtos(produto):
    return{**produto, 'preço': aumenta_dez_porcento(produto['preço'])}


novos_produtos = map(
    muda_preco_de_produtos,produtos
)
#novos_produtos = (x for x in produtos)

print_iter(produtos)
print_iter(novos_produtos)

print(novos_produtos)
print(hasattr(novos_produtos,'__iter__'))
print(hasattr(novos_produtos,'__next__'))
print(isinstance(novos_produtos, GeneratorType))

print(list(map(lambda x: x * 3, [1,2,3,4])))
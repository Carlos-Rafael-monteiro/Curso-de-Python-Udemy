# filter é um filtro funcional
def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preço': 10.00},
    {'nome': 'Produto 1', 'preço': 22.32},
    {'nome': 'Produto 3', 'preço': 10.11},
    {'nome': 'Produto 2', 'preço': 105.87},
    {'nome': 'Produto 4', 'preço': 69.90},   
]


def filtrar_preco(produto):
    return produto['preço'] > 20

'''novos_produtos = [
    p for p in produtos
    if p ['preço'] > 25
]'''
novos_produtos = filter(
    #lambda p: p ['preço'] > 25,
    filtrar_preco,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)
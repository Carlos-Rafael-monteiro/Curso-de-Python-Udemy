# Problemas dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente = adiciona_clientes('Rafael')
adiciona_clientes('Nicolly', cliente)
adiciona_clientes('Fernando', cliente)
cliente.append('Edu')
print(cliente)


cliente2 = adiciona_clientes('Gercila')
adiciona_clientes('Clara', cliente2)
print(cliente2)
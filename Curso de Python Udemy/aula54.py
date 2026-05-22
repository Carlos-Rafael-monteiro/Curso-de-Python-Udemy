'''
Faça uma lista de compras com lstas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índicee inexistentes na lista.
 '''

import os

lista_compras = []
print('-='*30)
print('Bem-vindo à lista de compras!')
print('-='*30)
while True:
    print('Selecione uma opção:')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista_compras.append(valor)


    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')
        try:
            indice = int(indice_str)
            del lista_compras[indice]
        except ValueError:
            print('Por favor, digite um número inteiro.')
        except IndexError:
            print('Índice não existe na lista')


    elif opcao == 'l':
        os.system('cls')
        if len(lista_compras) == 0:
            print('Nada para listar')
        for i, valor in enumerate(lista_compras):
            print(i, valor)

    elif opcao == 's':
        break
    else:
        print('Por favor, escolha i, a ou l.')
"""Calculadora com while"""
from time import sleep

while True:
    print('Calculadora')
    numero1 = input('Digite o primeiro número: ')
    operador = input('Digite o operador (+-/*): ')
    numero2 = input('Digite o segundo número: ')

    numero_validos = None
    # Verifica se os números são válidos
    # Se não forem válidos, continua o loop
    try:
        numero1 = float(numero1)
        numero2 = float(numero2) 
        numero_validos = True
    except:
        numero_validos = None

    if numero_validos is None:
        print('Um ou ambos os números são inválidos!')
        continue
    
    # Verifica se o operador é válido
    print('Calculando...')
    sleep(2)
    
    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue
    
    # Verifica se o operador tem mais de um
    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue
    
    # Realiza a operação

    if operador == '+':
        print(f'{numero1} + {numero2} = {numero1 + numero2}')
    elif operador == '-':
        print(f'{numero1} - {numero2} = {numero1 - numero2}')
    elif operador == '*':
        print(f'{numero1} * {numero2} = {numero1 * numero2}')
    elif operador == '/':
        print(f'{numero1} / {numero2} = {numero1 / numero2}')
    else:
        print('Operador inválido!')
    
    # Pergunta se o usuário quer sair
    sair = input('Quer sair: [s]im ou [n]ão: ').lower().startswith('s')
    if sair:
        break
    print('Continuando...')
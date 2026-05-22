# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, 
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False None [] {} ()
# Também existe o tipo None que é
# usado para representar um não valor

#entrada = input('[E]ntrar [S]air: ').upper()
#senha_digitada = input('Senha: ')

# if condição verdadeira True
#senha_permitida = '123456'
#if entrada == 'E' and senha_digitada == senha_permitida:
#    print('Entrar')
#else:
#    print('Sair')

# Avaliação de curto circuito
#print(True and False and True)

if 1 and 1:
    print(True and 1 and False)
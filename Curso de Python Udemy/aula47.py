'''
Faça um jogo para o usúario adivinhar qual a palavra secreta.
- Você vai propor ma palavra secreta qualquer e vai dar a 
possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra 
digitada está na palavra secreta.
...- se a letra digitado estiver na palavra secreta; exiba a letra
...- se a letra digitada não estiver na palavra secreta; 
exiba *.
- Faça a contagem de tentativas do seu usuário.
'''
import os

palavra_secreta = 'subaru'
letras_acertadas = ''
cont_tentativas = 0
while True:
    
    letra = input('Digite uma letra: ').lower()
    if len(letra) > 1:
        print('Digite apenas uma letra!')
        continue

    cont_tentativas += 1
    if letra in palavra_secreta:
        letras_acertadas += letra

    palavra_formada = ''    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada', palavra_formada)
    

    if palavra_formada == palavra_secreta: 
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print(f'Tentativas: {cont_tentativas}')
        letras_acertadas = ''
        cont_tentativas = 0
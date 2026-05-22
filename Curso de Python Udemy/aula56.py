'''
split e join com list e string
split - divide uma string
join - une uma string
'''
frase = 'Olha só que, coisa interessante'
lista_palavras = frase. split()  # Divide a string em uma lista de palavras
print(lista_palavras)
lista_frases = frase.split(',')  # Divide a string em uma lista de frases
print(lista_frases)

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip())


# Unindo uma lista de palavras em uma string
frase_unida = ' '.join(lista_palavras)  # Une a lista de palavras em uma string
print(frase_unida)
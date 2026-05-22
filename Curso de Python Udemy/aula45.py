'''
Iteráveis -> str, range, etc
iterador -> quem sabe entregar um valor por vez
next - > me entrega o próximo valor do iterador
iter - > me entrega seu iterador


numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)'''

texto = 'Luiz'
#iterador = iter(texto)  # iterador é um objeto que sabe entregar um valor por vez


#while True:
#   try:
#     print(next(iterador))  # next entrega o próximo valor do iterador
#    except StopIteration:
#        break  # quando não tem mais valores, o iterador gera uma excessão chamada StopIteration
for letra in texto:
    print(letra)  # o for já faz isso por baixo dos panos, ele chama o iter e o next para você  

'''
Cuidados com dados mutaveis
= - copiado o valor (imutaveis)
= - aponta para o mesmo valor na memoria (mutaveis)
'''

lista_a = ['Luiz', 'Maria']
lista_b = lista_a
lista_c = lista_a.copy()


lista_a[0] = 'Qualquer coisa'
print(lista_b)
print(lista_c)

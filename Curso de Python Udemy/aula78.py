# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# http://brasilescola.uol.com.br/matematica/conjunto.html
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set (iterável) oou {1, 2, 3}

#s1 = set() # set vazio
#s2 = {'Rafael', 1, 2, 3} # set com dados
#print(s1, type(s1)) # print set vazio
#print(s2, type(s2)) # print set com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão únicos:
# - Não aceitam valores mutáveis:
# - eles não tem índexes;
# - eles não garantem ordem;
# - eles são iteráveis ( for, in, not in)

# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# print(3 not in s1)
# print()
# print(2 in s1)
# print()
# for numero in s1:
#   print(numero)

# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Rafael')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
#s1.clear()
s1.discard('Olá mundo')

#print(s1)

# Operadores úteis:
# união | união(union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2
print(s3)
print()

s4 = s1 & s2
print(s4)
print()

s5 = s1 - s2
print(s5)
print()

s6 = s2 - s1
print(s6)
print()

s7 = s1 ^ s2
print(s7)


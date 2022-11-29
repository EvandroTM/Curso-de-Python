"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# nome = 'Evandro'
# noutra_variavel = nome 
# nome = 'Tozi'
# print(nome)
# print(noutra_variavel)

lista_a = ['Evandro', 'Isa']
lista_b = lista_a.copy() # para não apagar a lista anterior

lista_a[0] = 'Qualquer coisa'

print(lista_b)
print(lista_a)
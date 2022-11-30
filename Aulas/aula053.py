"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Evandro', 'Liliana', 'Edivaldo']
lista.append('João')

lista_enumerada = list(enumerate(lista))

print(lista_enumerada)

# for item in lista_enumerada:
#     print(item)
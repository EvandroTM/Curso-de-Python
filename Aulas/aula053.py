"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Evandro', 'Liliana', 'Edivaldo']
lista.append('João')

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)
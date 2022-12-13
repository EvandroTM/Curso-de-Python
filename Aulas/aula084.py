# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint

def p(v):
    pprint.pprint(novo__produtos, sort_dicts=False, width=40)

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 3
    for numero in range(10)
]
# print(list(range(10)))
# print(lista)

#mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},  
]

novo__produtos = [
    {**produto, 'preco': produto['preco'] *1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(novo__produtos)
# print(*novo__produtos, sep='\n')
# p(novo__produtos)
# lista = [n for n in range(10) if n < 5]
novo__produtos = [
    {**produto, 'preco': produto['preco'] *1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]
p(novo__produtos)

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""


lista = [10, 20, 30, 40]
numero = lista[2]
del lista[2]
print(lista)
lista.append(50)
lista.pop() # remove o item anterior , ultimo valor
lista.append(60)
lista.append('oi')
ultimo_valor = lista.pop() # ele remove o oi ... e mostra o que foi removido 
print(lista, 'Removido = ', ultimo_valor)
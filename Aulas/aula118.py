# Problemas dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista



cliente1 = adiciona_clientes('Evandro')
adiciona_clientes('Isabela', cliente1)
cliente1.append('teste')

cliente2 = adiciona_clientes('Edivaldo')
adiciona_clientes('Liliana', cliente2)

cliente3 = adiciona_clientes('Fabio')
adiciona_clientes('Rose', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)
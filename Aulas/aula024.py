# Operadores in e not in 
# Strings são interáveis 
# 0 1 2 3 4 5 6
# E V A N D R O 
# -7-6-5-4-3-2-1

# nome = 'Evandro'
# print(nome[2])
# print(nome[-5])
# print('a' in nome) #se estiver ele retorna True
# print('á' in nome)
# print(10 * '-')
# print('a' not in nome)
# print('á' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
'''
Fatiamento de Strings
012345678
Olá Mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da str
'''

variavel = 'Olá Mundo'
print(variavel[-4])
print(variavel[4])
print(variavel[4:8])
print(variavel[4:])
print(variavel[:8])
print(variavel[-8:-2])
print(variavel[3]) # Pegou caractere vazio ... imprimi vazio
print('---Len---')
print(len(variavel)) # checar tamanho de determina str
print(len(variavel[3]))
print(variavel[0:len(variavel):1])
print(variavel[0:9:2])
print(variavel[0:9:3]) # do 0 ao 9 pulando 3 
print(variavel[::-1])
print(variavel[-1:-10:-1])
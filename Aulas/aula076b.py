# Manipulando chaves e valores em dicionários

pessoa = {}

##
##
nome = input('Qual seu nome?: ')
sobrenome = input('Qual seu sobrenome?: ')

chave = 'nome'

pessoa[chave] =  nome
pessoa['Sobrenome'] = sobrenome

del pessoa['Sobrenome'] # como apagar chave
print(pessoa)
print(pessoa[chave])

# print(pessoa.get('Sobrenome'))
if pessoa.get('Sobrenome') is None:
    print('Não existe')

else:
    print(pessoa['Sobrenome'])


# print(pessoa['Sobrenome']) # vai ocorrer uma excessão aqui .. dapar resolver com try/except ou get

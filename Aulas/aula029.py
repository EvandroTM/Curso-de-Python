'''
Introdução ao try/except
try → tentar executar o código
except → ocorreu algum errro ao tentar executar
'''

# print(12345)
# print(67890)
# int('a')

numero_str = input('Vou dobra o número que você digitar: ')


try:
    print('STR', numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'O dobro de {numero_str} é {numero_float *2:.2f}')
except:
    print('Isso não é um número.')


#print(numero_str.isdigit()) # checa se o usuario digitou apenas números 


# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float *2:.2f}')
# else:
#     print('Isso não é um número.')
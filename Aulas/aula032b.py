'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada. ex Bom dia 0-11, Boa Tarde 12-17 e Boa noite 18-23.
'''

entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print('Bom Dia')
    elif hora >= 12 and hora <= 17:
        print('Boa Tarde')
    elif hora >= 18 and hora <=23:
        print('Boa Noite')
    else:
        print('Hora digitada está errada')
except:
    print('Por favor, digite um número inteiro!')
'''
Repetições
while(enquanto)
executa uma ação enquanto uma condição for verdadeira.
loop infinito → quando um código não tem fim.
'''

# condicao = True  loop infinito
# while condicao:
#     print(1)
#     print(2)
#     print(3)

condicao = True

while condicao:
    nome = input('Qual é o seu nome: ')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair':
        break

print('Fim')
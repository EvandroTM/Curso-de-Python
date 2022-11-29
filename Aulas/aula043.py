# senha_salva = '12345'
# senha_digitada = ''
# repeticoes = 0 


# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes +1}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas.')

texto = 'Python'

novo_texto = ''
for letra in texto: # variavel letra eu crio do além para que o for saiba aonde eu quero que ele jogue a resposta 
    novo_texto += f'*{letra}'
    print(letra) 

print(novo_texto + '*')




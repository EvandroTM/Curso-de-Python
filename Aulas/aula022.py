# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro, 
# a expressão inteira será avaliada naquele valor. 
# São considerados falsy (que vc ja viu)
# 0 0.0 ' ' False
# Também existe o tipo None que é usado para representar um não valor.

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permetida = '12345'

# if entrada == 'E' or entrada == 'e' and senha_digitada == senha_permetida: # pode ter quantos and eu quiser o programa sempre vai parar no FALSE
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto cirtcuito
senha = input('Senha: ') or 'Sem senha'
print(senha)
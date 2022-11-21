# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor. 
# São considerados falsy (que vc ja viu)
# 00.0 ' ' False
# Também existe o tipo None que é usado para representar um não valor.

entrada = input('[E]ntrar [S]air: ').upper()
senha_digitada = input('Senha: ')

senha_permetida = '12345'

if entrada == 'E' and senha_digitada == senha_permetida: # pode ter quantos and eu quiser o programa sempre vai parar no FALSE
    print('Entrar')
else:
    print('Sair')
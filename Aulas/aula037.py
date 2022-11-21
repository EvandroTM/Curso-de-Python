'''
Repetições
while(enquanto)
executa uma ação enquanto uma condição for verdadeira
Loop inifinito → quando um código não tem fim.
'''

contador = 0

while contador <= 10:
    contador += 1
    print(contador)

    if contador == 4:
        break
    
print('Fim')   
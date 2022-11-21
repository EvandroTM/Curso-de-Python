'''
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou - 
ex.: 0>-100,.1f
Conversion flags - !r !s !a 
'''
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{variavel:-^9}') # Preenchendo com o que eu quiser 
print(f'{1000.734893289438924392874:.2f}')
print(f'{1000.734893289438924392874:,.2f}')
print(f'{1000.734893289438924392874:+,.2f}')
print(f'{1000.734893289438924392874:0>+10,.2f}')
print(f'{1000.734893289438924392874:0=+10,.2f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
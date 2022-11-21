'''
https://docs.python.org/pt-br/3/library/stdtypes.html
imutáveis que vimos: str, int, float, bool
'''

string = 'Evandro TM'
outra_variavel = f'{string[:4]}ABC{string[4:]}'
# string[3] = 'ABC'
print(string)
print(outra_variavel)
print(string.capitalize())
print(string.upper())
print(string.zfill(100))
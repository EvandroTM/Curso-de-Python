'''
Iterável → str, range, etc (__iter__)
Iterador → quem sabe entrega um valor por vez
next → me entregue o próximo valor
iter → me entregue seu iterador
'''

# texto = iter('Evandro') # __iter__()
# print(next(texto)) # __next__()

texto = 'Evandro' # iterável
iterador = iter(texto) # iterador

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break

texto = 'Evandro' 
for letra in texto:
    print(letra)


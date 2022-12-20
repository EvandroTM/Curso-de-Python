# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

# def generator(n=0,):  # função que pode pausar!
#     yield 1  # Pausar 
#     print('Continuando...')
#     yield 2 # Pause
#     print('Mais uma...')
#     yield 3 # Pause
#     print('Vou terminar!')
#     return 'ACABOU'

# gen = generator(n=0)
# for n in gen:
#     print(n)

def generator(n=0, maximum=10): 
    while True:
        yield n
        n += 1

        if n > maximum: # para parar no 9 colocar >= 
            return

        

gen = generator(maximum=1000)
for n in gen:
    print(n)

'''from sys import path

import aula099_package.modulo  #1
from aula099_package.modulo import soma_do_modulo #2
from aula099_package import modulo #3
from aula099_package.modulo import * #4  # Má pratica 

# print(*path, sep='\n')

print(aula099_package.modulo.soma_do_modulo(1, 2)) #1
print(soma_do_modulo(1, 2)) #2
print(modulo.soma_do_modulo(1, 2)) #3
print(soma_do_modulo(1, 2)) #4
print(variavel) #4
print(nova_variavel) #4'''


# print(__name__)

# from aula099_package.modulo import soma_do_modulo

# import aula099_package
from aula099_package import soma_do_modulo, qualquer_coisa

# print(aula099_package.dobra(2))
print(soma_do_modulo(2, 3))
qualquer_coisa()



# # https://stackoverflow.com/questions/2386714/why-is-import-bad
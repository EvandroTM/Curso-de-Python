# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('Chamou o UPPER')
#         retorno = super().upper()
#         print('Depois do UPPER')
#         return retorno

# string = MinhaString('Evandro')
# print(string.upper())

class A(object):
    atributo_a = 'Valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'Valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'Valor c'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Ei burlei o sistema.')

    def metodo(self):
        # super().metodo()  # B
        # super(C, self).metodo()
        # super(B, self).metodo()
        # super(A, self).metodo() # Object
        A.metodo(self)
        B.metodo(self)
        print('C')


# print(C.mro())
# print(B.mro())
# print(A.mro())
c = C('Atributo', 'Outra coisa ')
print(c.atributo)
print(c.outra_coisa)
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
c.metodo()
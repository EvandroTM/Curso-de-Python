# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

# string = 'Evandro' # STR
# print(string.upper())
# print(isinstance(string, str))

# CriarBaseDeDados  # PascalCase

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Evandro', 'Moura')
# p1.nome = 'Evandro'
# p1.sobrenome = 'Moura'

p2 = Pessoa('Nome 2', 'sobrenome 2')
# p2.nome = 'teste'
# p2.sobrenome = 'teste 2'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)
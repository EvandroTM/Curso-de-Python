# Métodos em instâncias de classes de Python.
# Hard Coded - É algo que foi escrito diretamente no código.

class Carro:
    def __init__(self, nome):
        self.nome =  nome

    def acelerar(self):
        print(f'{self.nome} está acelerando... ')


string = 'Evandro'
print(string.upper())     

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()
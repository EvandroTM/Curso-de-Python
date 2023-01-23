#Classes decoradoras (Decorator classes)

class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador
          
    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna

    # def __init__(self, func):
    #     self.func = func
    #     self._multiplicador = 10

    # def __call__(self, *args, **kwargs):
    #     resultado = self.func(*args, **kwargs)
    #     return resultado * self._multiplicador


@Multiplicar(2)
def soma(x, y):
    return x + y

dois_mais_dois = soma(2, 4)
print(dois_mais_dois)

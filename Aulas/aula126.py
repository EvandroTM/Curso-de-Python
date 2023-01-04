# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

dados = {'nome': 'Evandro', 'idade': 34}
p1 = Pessoa(**dados)
# p1.nome = 'Eita'
# del p1.nome
# print(p1.nome)
# print(p1.idade)
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'Eita'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1)) # igual dict
# print(p1.outra)
print(vars(p1))
print(p1.nome)
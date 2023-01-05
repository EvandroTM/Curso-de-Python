# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        # setter
        self.user = user
    
    def set_passowrd(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connetion = cls()
        connetion.user = user
        connetion.password = password
        return connetion

    @staticmethod  # nao tem acesso ao self nem ao cls 
    def log(msg):
        print('LOG →', msg)

def connection_log(msg):  # outra forma de fazer 
        print('LOG →', msg)

# c1 = Connection()
c1 = Connection.create_with_auth('Evandro', '1234567')
# c1.set_user('Evandro')
# c1.set_passowrd('123')
print(Connection.log('Essa é a mensagem de log'))
print(c1.user)
print(c1.password)
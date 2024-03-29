class Conta:

    def __init__(self, numero ,titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.__saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}". format(self.__saldo))
        self.titular
    
    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self):
        valor_disponivel_a_sacar = self.__saldo + self.limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite".format(valor))

    def transfere(self, valor, origem, destino):
        origem.saca(valor)
        destino.deposita(valor)
    @property
    def get_saldo(self):
        return self.__saldo
    @property
    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    @staticmethod
    def codigo_banco():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
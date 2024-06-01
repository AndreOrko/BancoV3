class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico
    

    def saldo(self):
        pass
    

    def nova_conta(self, cliente, numero):
        pass


    def sacar(self, valor):
        pass


    def depositar(self, valor):
        pass


class ContaCorrente(Conta):
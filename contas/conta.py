from cliente.cliente import Cliente


class Conta:
    def __init__(self, cliente: object, numero: str, saldo: float):
        self._cliente = cliente
        self._numero = numero
        self._saldo = saldo

        if(self.__class__ is Conta):
            raise TypeError('Conta não pode ser instanciada diretamente!')

    def _sacar(self, valor: float, taxa: float):
        saque_total = valor * taxa
        if(saque_total > self._saldo):
            raise ValueError('Saldo insuficiente!')
        else:
            self._saldo -= saque_total

    def sacar(self, valor):
        raise TypeError('Metodo não implementado!')

    def depositar(self, valor):
        if(valor <= 0):
            raise ValueError('Valor invalido!')
        else:
            self._saldo += valor

    def transferir(self, valor, conta):
        if(valor > 0 and isinstance(conta, Conta)):
            self._sacar(valor, 0)
            conta.depositar(valor)

    @property
    def cliente(self):
        return self._cliente

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return (f'R$ {self._saldo:.2f}')

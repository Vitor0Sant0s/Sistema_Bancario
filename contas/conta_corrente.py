# from re import T
from .conta import Conta
from cliente.cliente import Cliente


class ContaCorrente(Conta):
    def __init__(self, cliente: object, numero: str, saldo: float):
        super().__init__(cliente, numero, saldo)
        if(Cliente.valida_cliente(self.cliente)):
            pass
        else:
            raise Exception(
                'Cliente invalido, verifique se os dados do cliente estão corretos!')

    def sacar(self, valor):
        taxa = 0.10 if valor >= 100.0 else 0.05
        self._sacar(valor, taxa)

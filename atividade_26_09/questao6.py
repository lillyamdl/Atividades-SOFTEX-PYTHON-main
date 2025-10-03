from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self,saldo):
        self.saldo = saldo

    @abstractmethod
    def sacar(self,valor):
        pass

    def verificar_saldo(self):
        return print(f"Saldo = {self.saldo}")

class ContaCorrente(ContaBancaria):
    def sacar(self,valor):
        if valor < self.saldo:
            print(f"saldo insuficiente")
        else:
            self.saldo -= valor
            print(f"seu saldo agora é : {self.saldo}")

contas = [
    ContaCorrente(10000),
    ContaCorrente(500)
]

for i, contas in enumerate(contas, start=1):
    contas.verificar_saldo()
    contas.sacar(500)
    contas.verificar_saldo()


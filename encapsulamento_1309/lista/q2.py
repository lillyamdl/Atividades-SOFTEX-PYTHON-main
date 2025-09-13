class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.__saldo = saldo
    
    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Deposito de r${valor} realizado")
        else:
            print("valor invalido")
    
    def sacar(self,valor):
        if 0< valor <= self.__saldo:
            self.__saldo -= valor
            print(f"saque de {valor} realizado")
        else:
            print("saldo insuficiente ou valor invalido")
    
    def ver_saldo(self):
        return self.__saldo

conta = ContaBancaria("Lila", 100)
conta.depositar(50)
print(conta.ver_saldo())
conta.sacar(50)
print(conta.ver_saldo())
conta.sacar(200)

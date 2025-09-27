class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
class Contabancaria:
    def __init__(self, numero, cliente:Cliente):
        self.numero = numero
        self.cliente = cliente
    
conta = Contabancaria("1234", Cliente("lila", "123.123.123-12"))
print(f"O cliente {conta.cliente.nome} possui a conta de numero {conta.numero}")
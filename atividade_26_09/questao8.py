from abc import ABC, abstractmethod
from datetime import date

# Classe abstrata
class Pessoa(ABC):
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    @abstractmethod
    def detalhes_de_cadastro(self):
        pass


# Classe concreta Cliente
class Cliente(Pessoa):
    def __init__(self, id, nome, data_cadastro=None):
        super().__init__(id, nome)
        self.data_cadastro = data_cadastro or date.today()

    def detalhes_de_cadastro(self):
        print(f"[Cliente] ID: {self.id}, Nome: {self.nome}, Data de Cadastro: {self.data_cadastro}")


# Classe concreta Fornecedor
class Fornecedor(Pessoa):
    def __init__(self, id, nome, cnpj):
        super().__init__(id, nome)
        self.cnpj = cnpj

    def detalhes_de_cadastro(self):
        print(f"[Fornecedor] ID: {self.id}, Nome: {self.nome}, CNPJ: {self.cnpj}")


# Função que recebe lista de Pessoa
def listar_cadastros(lista_pessoas):
    for pessoa in lista_pessoas:
        pessoa.detalhes_de_cadastro()


# Exemplo de uso
clientes_fornecedores = [
    Cliente(1, "Maria"),
    Cliente(2, "João", date(2025, 10, 2)),
    Fornecedor(3, "Supermercado ABC", "12.345.678"),
    Fornecedor(4, "Farmácia XPTO", "98.765.432")
]

listar_cadastros(clientes_fornecedores)

class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self,departamento):
        self.departamento = departamento
        super().__init__(nome,salario)

    def mostrar_informacoes(self):
        
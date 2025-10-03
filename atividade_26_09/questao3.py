class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self,nome,salario, departamento):
        self.departamento = departamento
        super().__init__(nome,salario)

    def mostrar_informacoes(self):
        return print(self.nome,self.salario,self.departamento)
    
pessoa1 = Gerente("lillya",1600,"departamento1")
pessoa1.mostrar_informacoes()
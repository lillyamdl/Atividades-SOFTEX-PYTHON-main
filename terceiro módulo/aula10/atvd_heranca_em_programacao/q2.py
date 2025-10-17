class Funcionario:
    def bonus(self):
        return 10

class Gerente(Funcionario):
    def bonus(self):
        return 20

class Programador(Funcionario):
    def bonus(self):
        return 25

funcionario = Funcionario()
gerente = Gerente()
programador = Programador()
print(funcionario.bonus())
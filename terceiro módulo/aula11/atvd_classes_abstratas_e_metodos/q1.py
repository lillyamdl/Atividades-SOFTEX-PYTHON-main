from abc import ABC, abstractmethod

class Funcionario(ABC):
    @abstractmethod
    def calcular_bonus(self):
        bonus = 0
        return bonus
        pass

class Gerente(Funcionario):
    def calcular_bonus(self,salario):
        bonus = salario * 10
        return bonus

class Desenvolvedor(Funcionario):
    def calcular_bonus(self,salario):
        bonus = salario * 20
        return bonus

gerente = Gerente()
desenvolvedor = Desenvolvedor()
print(gerente.calcular_bonus(1000))
print(desenvolvedor.calcular_bonus(1000))

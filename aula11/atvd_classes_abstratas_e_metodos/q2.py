from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass
    
    @abstractmethod
    def frear(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        print(f"Carro acelerando")
    def frear(self):
        print(f"Carro freando")

class Moto(Veiculo):
    def acelerar(self):
        print("Moto acelerando")
    def frear(self):
        print("Moto freando")

carro = Carro()
moto = Moto()
carro.acelerar()
moto.frear()
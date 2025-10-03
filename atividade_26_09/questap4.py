from abc import ABC, abstractmethod

class Veiculo(ABC):
    @property
    @abstractmethod
    def acelerar(self):
        pass

    def rodas(self):
        pass

class Carro(Veiculo):
    @property
    def rodas(self):
        return 4
    
    def acelerar(self):
        return print("o carro está acelerando")
    
class Moto(Veiculo):
    @property
    def rodas(self):
        return 2
    def acelerar(self):
        return print("a moto está acelerando")

carro = Carro()
moto = Moto()

print(f"O carro tem {carro.rodas} rodas e a moto tem {moto.rodas} rodas")
carro.acelerar()
moto.acelerar()

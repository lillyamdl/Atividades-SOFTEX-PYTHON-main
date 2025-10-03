from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
    
class Retangulo(FormaGeometrica):
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura

r = Retangulo(2,2)
print(f"Area:", r.calcular_area())


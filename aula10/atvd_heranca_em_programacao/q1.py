class Veiculo:
    def __init__(self,marca,ano):
        self.marca = marca
        self.ano = ano
    
class Carro(Veiculo):
    def __init__(self,rodas):
        self.rodas = rodas
        rodas = 4
    
    def ligar(self):
        print(f"ligado")
    
    def desligar(self):
        print(f"desligado")

class Moto(Veiculo):
    def __init__(self,rodas):
        self.rodas = rodas
        rodas = 2
    
    def ligar(self):
        print(f"moto: Ligado")
    
    def desligar(self):
        print(f"moto: Desligado")

carro = Carro("fusca",2010,4)


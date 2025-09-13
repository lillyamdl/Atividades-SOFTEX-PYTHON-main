class Carro:
    def __init__(self,modelo,velocidade):
        self.modelo = modelo
        self.__velocidade = velocidade
    
    def acelerar(self,valor):
        self.__velocidade += valor

    def frear(self,valor):
        if self.__velocidade - valor >= 0:
            self.__velocidade -= valor
        if self.__velocidade - valor <0:
            self.__velocidade = 0
            print("o carro ja esta parado")
        elif valor < 0:
            print("valor invalido")

carro = Carro("Fusca",40)
carro.acelerar(20)
print(carro._Carro__velocidade)
carro.frear(10)
print(carro._Carro__velocidade)
carro.frear(100)
print(carro._Carro__velocidade)
carro.frear(-10)

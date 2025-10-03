from abc import ABC, abstractmethod

class Percurso(ABC):
    @abstractmethod
    def tempo_estimado(self,distancia):
        pass

class Cobranca(ABC):
    @abstractmethod
    def calcular_tarifa(self,distancia):
        pass

class Taxi(Percurso,Cobranca):
    def __init__(self,velocidade_media = 40,tarifa_base = 10, tarifa_km = 2.0):
        self.velocidade_media = velocidade_media
        self.tarifa_base = tarifa_base
        self.tarifa_km = tarifa_km
    
    def tempo_estimado(self, distancia):
        tempo_horas = distancia / self.velocidade_media
        return tempo_horas * 60

    def calcular_tarifa(self, distancia):
        return self.tarifa_base + (distancia * self.tarifa_km)

taxi = Taxi()
distancia = 10
print(f"tempo estimado em minutos: {taxi.tempo_estimado(distancia)}")
print(f"tarifa: {taxi.calcular_tarifa(distancia)}")

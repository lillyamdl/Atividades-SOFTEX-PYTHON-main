import abc from ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def desenhar(self):
        "Desenha a forma"
        pass

class Circulo(Forma):
    def desenhar(self):
        return "Desenhando circulo"

class Quadrado(Forma):
    def desenhar(self):
        return "Desenhando quadrado"

class Triangulo(Forma):
    def desenhar(self):
        return "Desenhando triangulo"


def desenhar_formas(formas):
    resultados = []
    for forma in formas:
        resultados.append(forma.desenhar())
        return resultados


circulo = Circulo()

    



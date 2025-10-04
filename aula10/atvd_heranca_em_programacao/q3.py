class Nadador:
    def nadar(self):
        print("Nadando")
class Corredor:
    def correr(self):
        print("Correndo...")

class Triatleta(Nadador, Corredor):
    def mostrar(self):
        self.nadar()
        self.correr()

atleta = Triatleta()
atleta.mostrar()
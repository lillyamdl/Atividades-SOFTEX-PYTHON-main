class Animal:
    def __init__(self,nome):
        self.nome = nome
    
    def emitir_som(self):
        return "Som genérico!"

class Cachorro(Animal):
    def emitir_som(self):
        return "Latido!"

animal = Animal("zumano")
print(animal.emitir_som())
cachorro = Cachorro("rex")
print(cachorro.emitir_som())
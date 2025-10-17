class Passageiro:
    def __init__(self,nome,telefone,historico=[]):
        self.nome = nome
        self.telefone = telefone
        self.historico = historico
    
    def adicionar_historico(self,viagem):
        self.historico.append(viagem)


class Motorista:
    def __init__(self,cnh,placa,avaliacao_media=0):
        self.cnh = cnh
        self.placa = placa
        self.avaliacao_media = avaliacao_media
    
    def calcular_valor_corrida(self,distancia,tempo):
        valor = distancia * tempo
        return valor
    
    def registrar_pagamento(self,valor):
        print(f"Pagamento de R$ {valor} registrado")

passageiro = Passageiro("lila", 11, [2])
motorista = Motorista(1234, "ABC",3.6)
passageiro.adicionar_historico(3)
valor = motorista.calcular_valor_corrida(10,5)
print(passageiro.nome)
motorista.registrar_pagamento(valor)


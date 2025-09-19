class Time:
    def __init__(self, jogadores):
        self.jogadores = jogadores
    
time1 = Time(["jogador1", "jogador2", "jogador3"])
time2 = Time(["jogador4", "jogador5", "jogador6"])
time3 = Time(["jogador7", "jogador8", "jogadora9"])
print(time1.jogadores)
print(time2.jogadores)
print(time3.jogadores)
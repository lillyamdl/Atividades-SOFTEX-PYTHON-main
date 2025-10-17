class Musica:
    def __init__(self,musica):
        self.musica=musica

class Playlist:
    def __init__(self,musica):
        self.musica=musica
        self.musicas=[]
    
    def adicionar_musica(self,musica:Musica):
        self.musicas.append(musica)

adicionar_musica(Musica("musiquinha"))
adicionar_musica(Musica("musicaço")))
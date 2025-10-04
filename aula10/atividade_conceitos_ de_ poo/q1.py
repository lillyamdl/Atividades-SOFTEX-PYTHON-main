class Livro:
    def __init__(self,titulo,ibsn,paginas):
        self.titulo = titulo
        self.ibsn = ibsn
        self.paginas = paginas
    
    def registrar_livro(self):
        print(f"Livro {self.titulo} registrado")
    
    def emprestar(self,nome):
        print(f"Livro {self.titulo} emprestado para {nome}")
    

class Autor:
    def __init__(self,nome,nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

    def encontrar_livro(self,titulo):
        print(f"Livro {titulo} encontrado")

livro1 = Livro("livro1", "123", 200)
livro2 = Livro("livro2", 456, 300)
autor1 = Autor("autor1", "brasileiro")
autor2 = Autor("autor2", "cubano")
livro1.registrar_livro()
livro2.registrar_livro()
livro1.emprestar("lila")
livro2.emprestar("joao")
autor1.encontrar_livro("livro1")
autor2.encontrar_livro("livro2")

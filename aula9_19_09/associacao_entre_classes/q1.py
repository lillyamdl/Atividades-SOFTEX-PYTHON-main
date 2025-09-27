class Autor:
    def __init__(self, nome, nacionalidade):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
    
    def get_nome(self):
        return self.__nome
    
    def get_nacionalidade(self):
        return self.__nacionalidade
    
class Livro:
    def __init__(self,titulo,autor:Autor):
        self.__titulo = titulo
        self.__autor = autor
    
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor

# Instanciando objetos das classes corretamente
autor01 = Autor("autor1", "ingles")
autor02 = Autor("autor2", "brasileiro")
livro1 = Livro("livro1", autor01)
livro2 = Livro("livro2", autor02)
livro3 = Livro("livro3", autor02)

print(f"O livro '{livro1.get_titulo()}' foi escrito por {livro1.get_autor().get_nome()} ({livro1.get_autor().get_nacionalidade()})")
print(f"O livro '{livro2.get_titulo()}' foi escrito por {livro2.get_autor().get_nome()} ({livro2.get_autor().get_nacionalidade()})")
print(f"O livro '{livro3.get_titulo()}' foi escrito por {livro3.get_autor().get_nome()} ({livro3.get_autor().get_nacionalidade()})")

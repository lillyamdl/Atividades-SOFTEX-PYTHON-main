class Aluno:
    def __init__(self,nome,nota):
        self.nome = nome
        self.__nota = nota
    
    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def nota(self,valor):
        if 0 <= valor <= 10:
            self.__nota = valor
        else:
            print("nota invalida")

aluno = Aluno("lila", 8)
print(aluno.nota)
aluno.nota = 11
aluno.nota = -1
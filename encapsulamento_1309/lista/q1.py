class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.__preco = preco
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self,novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("preço inválido, tente novamente")

produto = Produto("Caneta", 2.5)
print(produto.preco)
produto.preco = -5
print(produto.preco)
produto.preco = 3
print(produto.preco)
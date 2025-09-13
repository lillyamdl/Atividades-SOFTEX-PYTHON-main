class Usuario:
    def __init__(self,senha,email):
        self.__senha = senha
        self.email = email
    
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self,valor):
        if len(valor) >= 6:
            self.__senha = valor
        else:
            print("falta de caracteres")
    
    def verificar_senha(self,tentativa):
        if tentativa == self.__senha:
            return True
        else:
            return False

usuario = Usuario("minhasenha","usuario@gmail")
print(usuario.senha)
usuario.senha = "123"
print(usuario.verificar_senha("minhasenha"))

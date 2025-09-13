# Implemente a busca linear que diga se o elemento existe ou não em uma lista de números.

lista = [1,2,3,4,5]

def busca_linear(lista,valor):
    for i in range (len(lista)):
        if lista [i] == valor:
            return i #retorna a posicao
        
    return -1 #retorna -1 se n achar

print(busca_linear(lista,6))

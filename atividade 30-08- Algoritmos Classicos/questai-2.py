#Modifique a busca linear para mostrar quantas vezes o valor aparece na lista.

def busca_linear(lista,valor):
    for i in range (len(lista)):
        if lista [i] == valor:
            contador = 0
            contador += 1
            return i #retorna a posicao
        
    return -1 #retorna -1 se n achar

lista = [1,2,3,3,4,5]

print(busca_linear(lista,3))
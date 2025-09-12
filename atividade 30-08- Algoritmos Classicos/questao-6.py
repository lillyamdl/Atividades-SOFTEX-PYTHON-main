#Escreva uma função recursiva que conte quantos elementos existem em uma lista.

def funcao_recursiva(lista):
    if lista == []:
        return 0
    else:
        return 1 + funcao_recursiva(lista[1:]) #chama ela mesma ate a lista ser vazia
    
print(funcao_recursiva([1,2,3,3,5]))
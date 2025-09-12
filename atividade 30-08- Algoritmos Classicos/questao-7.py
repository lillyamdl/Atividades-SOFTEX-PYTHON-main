# Crie um programa que pergunte ao usuário 5 números, salve em uma lista e:

#Mostre a lista ordenada (usando sort() e sorted())
#Procure um número escolhido pelo usuário na lista usando busca linear

def busca_linear(lista,valor):
    for i in range (len(lista)):
        if lista [i] == valor:
            return i
    return -1

numeros = []

for i in range(5):
    num = int(input("coloque seus numeros:"))
    numeros.append(num)

print(sorted(numeros))
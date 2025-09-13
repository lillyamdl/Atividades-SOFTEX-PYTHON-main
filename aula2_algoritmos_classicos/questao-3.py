# Implemente o Bubble Sort em ordem decrescente.

def bubble_sort(lista):
    qntd = len(lista)
    for i in range(qntd):
        for j in range(0,qntd-i-1):
            if lista [j] > lista[j+1]:
                lista [j], lista[j+1] = lista [j+1], lista[j]
    return lista

valores = [1,2,4,5,7,3,6]

print(list(reversed(bubble_sort(valores))))

#Crie uma função que filtra números pares de uma lista.

def naoEhPar(num):
    return num % 2 != 0

lista = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(naoEhPar,lista))) #o filter retorna um objeto iteravel, por isso converte pra lista
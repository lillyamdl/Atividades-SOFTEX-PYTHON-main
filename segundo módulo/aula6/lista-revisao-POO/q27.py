#Condicionais + Laços : Verifique se todos os números em uma lista são positivos.

lista = [1.-2,3,4,-5]
positivos = True

for numero in lista:
    if numero < 0:
        positivos = False
        break


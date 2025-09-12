#Escreva uma função recursiva que calcule a potência (ex.: 2^3 = 8).

def potencia(base,expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base,expoente-1) #chama ela mesma ate o expoente ser 0
print(potencia(2,3))
vogais = "aeiou"

def contarVogais(contar):
    num_v = 0
    for char in contar:
        if char in vogais:
            num_v += 1
    return num_v

nome = input()
print(contarVogais(nome))
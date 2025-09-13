#contar vogais e consoantes

vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"
def contador (contar):
    vogais = "aeiou"
    consoantes = "bcdfghjklmnpqrstvwxyz"
    num_v = 0
    num_c = 0
    lower = frase.lower()

    for char in lower:
        if char.isalpha():
            if char in vogais:
                num_v += 1
            elif char in consoantes:
                num_c += 1

    return num_v, num_c

frase = input()
a , b = contador(frase)
print(f"A frase contém {vogais} vogais e {consoantes} consoantes")
vogais = "aeiou"
def contador(palavra):
    num_v = 0
    for char in palavra:
        if char in vogais:
            num_v += 1
    return num_v
palavra = input()
a = contador(palavra)
print(f"a palavra tem {a} vogais")
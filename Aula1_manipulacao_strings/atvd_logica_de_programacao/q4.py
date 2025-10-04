frase = input()
frase_limpa = frase.replace(" " , "").lower()

if frase_limpa == frase_limpa[::-1]:
    print("É um palíndromo")
else:
    print("Não é")
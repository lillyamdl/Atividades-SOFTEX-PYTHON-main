#frequencia de palavras

frase = input()
frase_separada = frase.split()
frequencia = {}

for palavra in frase_separada:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1
    
for palavra, contagem in frequencia.items():
    print(f"{palavra}: {contagem}")
    
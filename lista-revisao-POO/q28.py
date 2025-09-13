#Strings + Dicionários : Conte a ocorrência de cada palavra em uma frase (ignore guardadas/minúsculas).

frase = input("digite uma frase: ").lower().split()
dicionario = {} #o dicionari vazio é criado fora do for para nao ser reiniciado a cada loop
for palavra in frase:
    if palavra in dicionario:
        dicionario[palavra] += 1  #ele busca se no dicionario, a palavra da frase ja existe nele
    else:
        dicionario[palavra]=1 #se nao existir, ele cria uma nova chave com valor 1

print(dicionario)
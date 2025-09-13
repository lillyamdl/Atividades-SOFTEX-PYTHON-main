#gerar acrônimo

entrada = input()

stopwords = ("da" , "de" , "do", "das" , "dos" , "e")

separar=entrada.split()
acronimo = ""

for palavra in separar:
    if palavra.lower() not in stopwords: 
        acronimo += palavra[0].upper()

print(acronimo)
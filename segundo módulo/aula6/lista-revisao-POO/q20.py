#mix de conceitos
# Listas + Dicionários : Transforme duas listas (uma de chaves, outra de valores) em um dicionário.

lista_chaves = ["chave1", "chave2"]
lista_valores = ["valor1", "valor2"]

meu_dicionario=(dict(zip(lista_valores,lista_chaves)))
print(meu_dicionario)
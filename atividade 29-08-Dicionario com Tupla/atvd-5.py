produto = input("qual produto?")
tamanho = input("qual tamanho?")

precos = {
    ('camiseta' , 'p') : 20,
    ('camiseta' , 'm') : 25,
    ('calca' , 'p') : 30,
    ('calca', 'm') : 35
}

chave_produto = (produto, tamanho) #vc cria ela pra usar como chave, e ele procurar dentro do dicionario

if chave_produto in precos:
  preco_correspondente = precos[chave_produto]
  print(f"O preço para {produto} tamanho {tamanho} é: {preco_correspondente}")
else:
  print('nao encontrando')
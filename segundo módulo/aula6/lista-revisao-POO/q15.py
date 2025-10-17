def contar(palavra):
    frequencia = {} #se cria um dicionario vazio para guardar as frequencias
    for letra in palavra: #percorre a palavra letra por letra
        if letra in palavra: #verifica se ela ja é uma chave no dicionario
            frequencia[letra] += 1 #se ela for, ele adiciona nela mais um, ou seja, nona, dois n, +=2
        else:
            frequencia[letra] = 1 #se ela nao for, ele coloca ela no dicionario com o valor 1, ou seja, se tiver so um vai ficar 1
        return frequencia

palavra = 'hello'
resultado = contar(palavra)
print(resultado)

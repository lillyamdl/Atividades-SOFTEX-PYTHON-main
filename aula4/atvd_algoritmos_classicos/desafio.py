def programa_completo():
    lista = []
    qtd = int(input("Quantos números deseja inserir? "))
    for i in range(qtd):
        n = int(input(f"Digite o {i+1}º número: "))
        lista.append(n)

    print("\nLista original:", lista)
    print("Lista ordenada:", sorted(lista))

    valor = int(input("\nDigite um valor para buscar na lista: "))
    if valor in lista:
        print(f"O número {valor} está na lista!")
        print(f"Fatorial de {valor} é {fatorial(valor)}")
    else:
        print(f"O número {valor} não está na lista.")

programa_completo()
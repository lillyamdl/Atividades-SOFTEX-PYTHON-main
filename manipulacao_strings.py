def verificar_palavra(palavra):
    """Verifica as propriedades de uma palavra e retorna suas classificações."""
    comeca_com_a = palavra.lower().startswith('a')
    e_palindromo = palavra == palavra[::-1]
    e_longa = len(palavra) > 7
    e_comum = not (comeca_com_a or e_palindromo or e_longa)

    if comeca_com_a:
        print(f"{palavra}: Começa com A")
    elif e_palindromo:
        print(f"{palavra}: É palíndromo")
    elif e_longa:
        print(f"{palavra}: Palavra longa")
    else:
        print(f"{palavra}: Palavra comum")

    return comeca_com_a, e_palindromo, e_longa, e_comum


entrada_usuario = input("Digite várias palavras separadas por espaço: ")
lista_palavras = entrada_usuario.split()


contador_comeca_com_a = 0
contador_palindromos = 0
contador_longas = 0
contador_comuns = 0


print("\n--- Análise das palavras ---")
for palavra in lista_palavras:

    a, pal, long, com = verificar_palavra(palavra)

    # Atualiza os contadores do resumo
    if a:
        contador_comeca_com_a += 1
    if pal:
        contador_palindromos += 1
    if long:
        contador_longas += 1
    if com:
        contador_comuns += 1

print("\n--- Resumo ---")
print(f"Total de palavras que começam com A: {contador_comeca_com_a}")
print(f"Total de palavras que são palíndromos: {contador_palindromos}")
print(f"Total de palavras longas: {contador_longas}")
print(f"Total de palavras comuns: {contador_comuns}")

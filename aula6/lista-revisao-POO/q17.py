#Condicionais + Strings: Verifique se uma string é um palíndromo (ex: "radar").
def ehPalindromo(ex):
    if ex == ex[::-1]:
        print("eh palindromo")
    else:
        print("nao eh palindromo")

palavra = input()
ehPalindromo(palavra)


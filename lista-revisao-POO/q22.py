#Crie um menu simples onde o usuário escolhe opções (ex: 1-ver estoque, 2-adicionar item).

menu = {
    1: "ver estoque",
    2: "adicionar item"
}

print("Menu:", menu)
opcao = int(input("escolha uma opção"))
if opcao ==1:
    print("ver estoque")
elif opcao ==2:
    print("adicionar item")

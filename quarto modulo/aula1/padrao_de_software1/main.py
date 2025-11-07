from models.cliente import Cliente
from dao.cliente_dao import ClienteDAO
from models.produto import Produto
from dao.produto_dao import ProdutoDAO

dao = ClienteDAO()

def listar(Produto, Cliente):
    produtos = ProdutoDAO()
    clientes = ClienteDAO()
    print("Produtos:")
    for p in produtos.listar():
        print(p)
    print("\nClientes:")
    for c in clientes.listar():
        print(c)


def run_menu():
    while True:
        print("\n1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            cliente = Cliente(nome, email)
            dao.salvar(cliente)
            print("✅ Cliente cadastrado!")
        elif opcao == "2":
            clientes_dao = dao.listar()
            for c in clientes_dao:
                print(c)
        elif opcao == "3":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    run_menu()
from app1.db import Database
from app1.cliente_repo import ClienteRepository

def main():
    db = Database()
    repo = ClienteRepository(db)

    print("=== criar novo cliente ===")
    nome = input("nome:")
    email = input("email:")
    telefone = input("telefone:")
    cliente_id = repo.criar(nome,email,telefone)
    print(f"cliente criado com id :{cliente_id}")

    print("\n== BUSCAR CLIENTE POR ID ==")
    cliente = repo.buscar_por_id(cliente_id)
    if cliente:
        print(f"✅ Cliente encontrado: {cliente['nome']} - {cliente['email']} - {cliente['telefone']}")
    else:
        print(f"❌ Cliente com ID {cliente_id} não encontrado")

    print("\n==ATUALIZAR TELEFONE==")
    novo_tel = input("Novo telefone: ")
    afetadas = repo.atualizar_telefone(cliente_id, novo_tel)

    if afetadas > 0:
        print("Telefone atualizado!!!")
    else:
        print("id n encontrado bixa")
    
    print("\n == DELETAR ALLGUM CLIENTE ==")
    cliente_deletado = int(input("id do cliente: "))
    confirm = input("tem certeza q quer deletar esse cliente? S/N").strip().upper()
    if confirm == 'S':
        sucesso = repo.remover(int(cliente_id))
    else:
        print("operação cancelada")

    
    clientes = repo.listar_todos()
    print('\n== CLIENTES CADASTRADOS ==')
    for c in clientes:
        print(f"{c['id']} : {c['nome']} - {c['email']} - {c['telefone']} - {c['criado_em']}")

if __name__ == "__main__":
    main()
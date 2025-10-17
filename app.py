from stages import model_lead
import repo

def add_lead():
    name = input("Nome: ")
    company = input("Empresa: ")
    email = input("Email: ")

    repo.create(model_lead(name, company, email))
    print("\n Lead adicionado com sucesso!\n")

def list_leads():
    leads = repo._load()  # carrega os leads do arquivo JSON

    if not leads:
        print("\n Nenhum lead encontrado.\n")
        return

    print("\n=== LISTA DE LEADS ===")
    for i, lead in enumerate(leads, start=1):
        print(f"{i}. Nome: {lead['name']}")
        print(f"   Empresa: {lead['company']}")
        print(f"   Email: {lead['email']}")
        print(f"   Estágio: {lead['stage']}")
        print(f"   Criado em: {lead['created']}\n")

def main():
    while True:
        print_menu()
        op = input("Escolha: ")
        if op == "1":
            add_lead()
        elif op == "2":
            list_leads()
        elif op == "0":
            print(" Até mais!")
            break
        else:
            print("❌ Opção inválida, tente novamente.")

def print_menu():
    print("\n Mini CRM de Leads")
    print("[1] Adicionar lead")
    print("[2] Listar leads")
    print("[0] Sair")

if __name__ == "__main__":
    main()

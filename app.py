from stages import model_lead
import repo

def add_lead():
    name = input("Nome: ")
    company = input("Empresa: ")
    email = input("Email: ")

    repo.create(model_lead(name, company, email))
    print("Lead adicionar")

def list_leads():
    print("Listar leads")

def main():
    while True:
        print_menu()
        op = input("Escolha: ")
        if op == "1":
            add_lead()
        elif op == "2":
            list_leads()
        elif op == "0":
            print("Até mais")
            break
        else:
            print("opaão inválida")

def print_menu():
        print("\nMini CRM deLeads - (Adicionar/Listar)")
        print("[1] Adicionar lead")
        print("[2] Listar lead")
        print("[0] Sair")

if __name__ == "__main__":
    main()



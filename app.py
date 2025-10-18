from stages import Lead
from repo import LeadRepo
from typing import List

class CRMApp:
    """
    Classe principal que gerencia a lógica de negócios e a interface do Mini-CRM.
    """

    def __init__(self):
        """
        Inicializa o aplicativo, criando uma instância do Repositório.
        """
        # Atributo de instância: O Repositório é um componente crucial do aplicativo.
        self.repo = LeadRepo()

    def _get_all_leads(self) -> List[Lead]:
        """
        Método auxiliar para carregar e retornar todos os leads.
        """
        return self.repo.load_leads()

    def add_lead(self):
        """
        Coleta dados do usuário e adiciona um novo Lead ao repositório.
        """
        print("\n=== ADICIONAR NOVO LEAD ===")
        name = input("Nome: ")
        company = input("Empresa: ")
        email = input("Email: ")

        # Cria um novo objeto Lead
        new_lead = Lead(name, company, email)

        # Usa o método 'create' do Repositório para salvar o objeto
        self.repo.create(new_lead)
        print("\n✅ Lead adicionado com sucesso!\n")

    def list_leads(self):
        """
        Lista todos os Leads cadastrados.
        """
        leads = self._get_all_leads()

        if not leads:
            print("\n❌ Nenhum lead encontrado.\n")
            return

        print("\n=== LISTA DE LEADS ===")
        for i, lead in enumerate(leads, start=1):
            # Acessando os atributos do objeto Lead
            print(f"{i}. Nome: {lead.name}")
            print(f" Empresa: {lead.company}")
            print(f" Email: {lead.email}")
            print(f" Estágio: {lead.stage}")
            print(f" Criado em: {lead.created}\n")

    def search_leads(self):
        """
        Busca Leads por nome, empresa ou email.
        """
        leads = self._get_all_leads()

        if not leads:
            print("\n❌ Nenhum lead cadastrado para buscar.\n")
            return

        term = input("Digite o nome, empresa ou email para buscar: ").strip().lower()

        # Lista de Leads (objetos) que correspondem ao termo
        found = [
            lead for lead in leads
            if term in lead.name.lower() or
               term in lead.company.lower() or
               term in lead.email.lower()
        ]

        if not found:
            print(f"\n🔍 Nenhum lead encontrado para: '{term}'.\n")
            return

        print(f"\n=== RESULTADOS DA BUSCA ({len(found)}) ===")
        for i, lead in enumerate(found, start=1):
            print(f"{i}. Nome: {lead.name}")
            print(f" Empresa: {lead.company}")
            print(f" Email: {lead.email}")
            print(f" Estágio: {lead.stage}")
            print(f" Criado em: {lead.created}\n")

    def print_menu(self):
        """
        Exibe o menu principal.
        """
        print("\n=== Mini CRM de Leads (POO) ===")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Procurar lead")
        print("[0] Sair")

    def main(self):
        """
        Loop principal da aplicação.
        """
        while True:
            self.print_menu()
            op = input("Escolha: ")

            if op == "1":
                self.add_lead()
            elif op == "2":
                self.list_leads()
            elif op == "3":
                self.search_leads()
            elif op == "0":
                print(" Até mais!")
                break
            else:
                print("❌ Opção inválida, tente novamente.")

if __name__ == "__main__":
    # Instancia a classe CRMApp e chama seu método principal (main)
    app = CRMApp()
    app.main()
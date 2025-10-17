from pathlib import Path
import json
from typing import List, Dict
# Importamos a classe Lead para usá-la no repositório
from stages import Lead

class LeadRepo:
    """
    Gerencia a persistência de dados (salvar e carregar) dos Leads em um arquivo JSON.
    """

    def __init__(self, db_filename: str = "leads.json"):
        """
        Inicializa o Repositório, definindo o caminho do arquivo de banco de dados.
        """
        self.DATA_DIR = Path(__file__).resolve().parent
        self.DATA_DIR.mkdir(exist_ok=True)
        self.DB_PATH = self.DATA_DIR / db_filename # Atributo de instância

    def _load_raw_data(self) -> List[Dict]:
        """
        Método privado para carregar a lista de dicionários (dados brutos) do arquivo JSON.
        """
        if not self.DB_PATH.exists():
            return []
        try:
            # O .read_text() e json.loads() são implementados aqui, encapsulando a lógica de IO
            return json.loads(self.DB_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []

    def _save(self, leads: List[Dict]):
        """
        Método privado para salvar a lista de dicionários (dados brutos) no arquivo JSON.
        """
        self.DB_PATH.write_text(
            json.dumps(leads, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

    # Método público para interagir com a aplicação
    def load_leads(self) -> List[Lead]:
        """
        Carrega os Leads do JSON e retorna uma lista de objetos Lead.
        """
        raw_data = self._load_raw_data()
        # Converte cada dicionário em um objeto Lead
        return [Lead.from_dict(data) for data in raw_data]

    # Método público para interagir com a aplicação
    def create(self, lead: Lead):
        """
        Adiciona um novo objeto Lead ao repositório e o salva.
        """
        # Carrega a lista atual de Leads (como objetos)
        existing_leads = self.load_leads()

        # Adiciona o novo Lead (objeto)
        existing_leads.append(lead)

        # Converte a lista de objetos Lead de volta para dicionários para salvar
        raw_data_to_save = [l.to_dict() for l in existing_leads]

        self._save(raw_data_to_save)
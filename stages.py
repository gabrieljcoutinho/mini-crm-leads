from datetime import date
from typing import Dict

# Definição do estágio inicial para novos leads
INITIAL_STAGE = "Novo"

class Lead:
    """
    Representa um Lead no sistema CRM, com seus dados e estado inicial.
    """

    # Atributo de classe (opcional, mas bom para padronizar)
    _default_stage: str = INITIAL_STAGE

    def __init__(self, name: str, company: str, email: str, stage: str = None, created: str = None):
        """
        Construtor para inicializar um objeto Lead.

        Se 'stage' ou 'created' não forem fornecidos, usa valores padrão.
        """
        self.name = name  # Atributo de instância
        self.company = company  # Atributo de instância
        self.email = email  # Atributo de instância

        # Define o estágio, usando o padrão se não for fornecido
        self.stage = stage if stage is not None else self._default_stage

        # Define a data de criação
        if created is None:
            self.created = date.today().strftime("%d/%m/%Y")
        else:
            self.created = created

    def to_dict(self) -> Dict:
        """
        Retorna o Lead como um dicionário, útil para salvar no JSON.
        """
        return {
            "name": self.name,
            "company": self.company,
            "email": self.email,
            "stage": self.stage,
            "created": self.created,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Lead':
        """
        Método de classe para criar um objeto Lead a partir de um dicionário (JSON).
        """
        return cls(
            name=data.get("name"),
            company=data.get("company"),
            email=data.get("email"),
            stage=data.get("stage", cls._default_stage),
            created=data.get("created"),
        )
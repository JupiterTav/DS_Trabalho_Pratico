from abc import ABC, abstractmethod


class IGerador_arquivo(ABC):
    @abstractmethod
    def criar_arquivo(self, caminho: str) -> int:
        """Criar_arquivo Doc: Cria arquivo no caminho designado."""
        pass

    @abstractmethod
    def salvar_arquivo(self):
        """Salvar_arquivo Doc: Salva o arquivo gerado pela instancia do gerador em questão."""
        pass

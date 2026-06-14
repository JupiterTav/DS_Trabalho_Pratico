from abc import ABC, abstractmethod


class IGerador_arquivo(ABC):
    @abstractmethod
    def criar_arquivo(self, caminho: str) -> int:
        pass

    @abstractmethod
    def salvar_arquivo(self):
        pass

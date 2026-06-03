from abc import ABC, abstractmethod

from core.track import Track


class IGerenciador_arquivo(ABC):
    @abstractmethod
    def criar_arquivo(self, caminho: str) -> int:
        pass

    @abstractmethod
    def processar_arquivo(self, vozes: list[Track]):
        pass

    @abstractmethod
    def salvar_arquivo(self):
        pass



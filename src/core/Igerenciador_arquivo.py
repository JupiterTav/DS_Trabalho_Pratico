from abc import ABC, abstractmethod

from core.voz import Voz


class IGerenciador_arquivo(ABC):
    @abstractmethod
    def criar_arquivo(self, caminho: str) -> int:
        pass

    @abstractmethod
    def processar_arquivo(self, vozes: list[Voz]):
        pass

    @abstractmethod
    def salvar_arquivo(self):
        pass



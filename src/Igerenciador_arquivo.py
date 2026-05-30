from abc import ABC, abstractmethod

from src.gerador_vozes import GeradorVozes
from src.track import Track


class IGerenciador_arquivo(ABC):
    @abstractmethod
    def criar_arquivo(self, caminho: str) -> int:
        pass

    @abstractmethod
    def processar_arquivo(self, vozes: list[Track], global_vozes: GeradorVozes):
        pass

    @abstractmethod
    def salvar_arquivo(self):
        pass



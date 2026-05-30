from abc import ABC, abstractmethod


class IGerenciador_arquivo(ABC):
    @abstractmethod
    def criar_arquivo(self):
        pass

    @abstractmethod
    def processar_arquivo(self):
        pass

    @abstractmethod
    def salvar_arquivo(self):
        pass



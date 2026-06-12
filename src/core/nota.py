from abc import ABC, abstractmethod

class Nota(ABC):

    @abstractmethod
    def nota_comando(self):
        pass

    @abstractmethod
    def nota_comando_mido(self):
        pass
from abc import ABC, abstractmethod

class ICharacterVoz(ABC):
    def __init__(self, simbolo, voz):
        self.nota = simbolo
        self.voz = voz
    @abstractmethod
    def character_comando(self):
        pass

    @abstractmethod
    def character_comando_midi(self):
        pass
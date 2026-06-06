from abc import ABC, abstractmethod

class IInterpretador(ABC):

    @abstractmethod
    def interpretar_char(self, char: str):
        pass

    @abstractmethod
    def is_interpretavel(self, char: str) -> bool:
        pass
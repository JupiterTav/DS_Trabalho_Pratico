from typing import overload

import pygame.midi

from abc import ABC, abstractmethod

class ICharacter(ABC):
    def __init__(self, simbolo: int):
        self.nota = simbolo
    @abstractmethod
    def character_comando(self):
        pass

    @abstractmethod
    def character_comando_midi(self):
        pass
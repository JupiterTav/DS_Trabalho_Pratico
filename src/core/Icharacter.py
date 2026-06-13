from typing import overload

import pygame.midi

from abc import ABC, abstractmethod

class ICharacter(ABC):

    @abstractmethod
    def character_comando(self):
        pass

    @abstractmethod
    def character_comando_midi(self):
        pass
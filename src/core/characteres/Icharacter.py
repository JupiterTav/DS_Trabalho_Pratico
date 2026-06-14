
from abc import ABC, abstractmethod

from mido import Message, MetaMessage, MidiTrack

class ICharacter(ABC):
    def __init__(self, simbolo, voz):
        self.nota = simbolo
        self.voz = voz

    @abstractmethod
    def character_comando(self, track: MidiTrack) -> None | MetaMessage | Message:
        pass

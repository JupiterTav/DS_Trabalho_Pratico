from typing import override, overload
from mido import Message
import pygame.midi

from core.Icharacter import ICharacter

class CharacterNota(ICharacter):
    def __init__(self, nota):
        self.nota = nota

    @override
    def character_comando(self, volume: int, channel: int, output: pygame.midi.Output) -> None:
        output.note_on(self.nota, velocity=volume, channel=channel)

    @override
    def character_comando_midi(self, volume: int, channel: int, time: int) -> Message:
        return Message("note_on", note=self.nota, channel=channel, velocity=volume, time=time*480)
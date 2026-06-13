from typing import override
from mido import Message
import pygame.midi

from core.Icharacter import ICharacter

class CharacterNota(ICharacter):
    def __init__(self, nota):
        super().__init__(nota)

    def character_comando(self, volume: int, channel: int, output: pygame.midi.Output) -> None:
        super().character_comando()
        output.note_on(super().nota, velocity=volume, channel=channel)

    def character_comando_midi(self, volume: int, channel: int, time: int) -> Message:
        super().character_comando_midi()
        return Message("note_on", note=super().nota, channel=channel, velocity=volume, time=time*480)
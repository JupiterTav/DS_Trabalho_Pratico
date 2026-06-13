from typing import override
from mido import Message
import pygame.midi

from core.Icharacter import ICharacter


class CharacterPausa(ICharacter):
    def __init__(self, char):
        super().__init__(char)

    def character_comando(self, output: pygame.midi.Output, channel: int):
        super().character_comando()
        output.note_off(super().nota, velocity=0, channel=channel)
        pass
    
    def character_comando_midi(self, channel: int) -> Message:
        super().character_comando_midi()
        return Message("note_off", note=super().nota ,velocity=0, channel=channel)
        pass

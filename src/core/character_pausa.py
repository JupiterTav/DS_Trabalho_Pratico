from typing import override
from mido import Message
import pygame.midi

from core.Icharacter import ICharacter


class CharacterPausa(ICharacter):
    def __init__(self, char, output: pygame.midi.Output ,voz):
        super().__init__(char, output, voz)
        self.voz = voz

    def character_comando(self):
        super().character_comando()
        self.output.note_off(super().nota, velocity=0, channel=self.voz.channel)
        pass
    
    def character_comando_midi(self) -> Message:
        super().character_comando_midi()
        return Message("note_off", note=super().nota ,velocity=0, channel=self.voz.channel)
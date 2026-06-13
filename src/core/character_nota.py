from typing import override
from mido import Message
import pygame.midi

from core.Icharacter import ICharacter


class CharacterNota(ICharacter):
    def __init__(self, nota, output: pygame.midi.Output, voz):
        super().__init__(nota, output, voz)
        self.voz = voz

    def character_comando(self) -> None:
        super().character_comando()
        self.output.note_on(self.nota, velocity=self.voz.volume, channel=self.voz.channel)

    def character_comando_midi(self) -> Message:
        super().character_comando_midi()
        return Message("note_on", note=self.nota,
                       channel=self.voz.channel, velocity=self.voz.volume, time=self.voz.delay*480)
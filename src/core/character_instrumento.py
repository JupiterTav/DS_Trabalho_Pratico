import pygame.midi
from mido import Message

from core.Icharacter import ICharacter

class CharacterInstrumento(ICharacter):
    def __init__(self, char, output: pygame.midi.Output, voz):
        super().__init__(char, output, voz)

    def character_comando(self):
        super().character_comando()
        self.output.set_instrument(instrument_id=self.voz.instrumento, channel=self.voz.channel)


    def character_comando_midi(self) -> Message:
        super().character_comando_midi()
        return Message("program_change", channel=self.voz.channel, program=self.voz.instrumento)

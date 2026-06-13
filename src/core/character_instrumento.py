import pygame.midi
from mido import Message

from core.Icharacter import ICharacter

class CharacterInstrumento(ICharacter):
    def __init__(self, char):
        super().__init__(char)

    def character_comando(self, instrumento: int, channel: int,output: pygame.midi.Output):
        super().character_comando()
        output.set_instrument(instrument_id=instrumento, channel=channel)


    def character_comando_midi(self, channel: int, instrumento: int) -> Message:
        super().character_comando_midi()
        return Message("program_change", channel=channel, program=instrumento)

from typing import override

from mido import Message, MidiTrack

from core import config_mapeamento
from core.Icharacter import ICharacter

class CharacterInstrumento(ICharacter):
    def __init__(self, char, voz):
        super().__init__(char, voz)

    @override
    def character_comando(self, track: MidiTrack) -> None:
        if self.nota in config_mapeamento.gm_intruments:
            self.voz.instrumento = config_mapeamento.gm_intruments[self.nota]
        elif self.nota.isnumeric():
            valor = int(self.nota)
            self.voz.instrumento = self.voz.instrumento + valor if valor % 2 == 0 else 1
        track.append(Message("program_change", channel=self.voz.channel, program=self.voz.instrumento))

        return None

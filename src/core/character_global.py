from typing import overload, override

from mido import MetaMessage, MidiTrack, bpm2tempo

from core import config_mapeamento
from core.Icharacter import ICharacter


class CharacterGlobal(ICharacter):
    def __init__(self, char, voz):
        super().__init__(char, voz)
        self.variacao_bpm = 10

    @override
    def character_comando(self, track: MidiTrack):
        config_mapeamento.bpm_global += self.variacao_bpm if self.nota == '>' else self.variacao_bpm * -1
        track.append(MetaMessage('set_tempo', tempo=bpm2tempo(config_mapeamento.bpm_global), time=0))

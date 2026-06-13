from typing import overload

import pygame.midi
from mido import MetaMessage, bpm2tempo

from core import config_mapeamento
from core.Icharacter import ICharacter


class CharacterGlobal(ICharacter):
    def __init__(self, char, output: pygame.midi.Output, voz):
        super().__init__(char, output, voz)
        self.variacao_bpm = 10

    def character_comando(self):
        config_mapeamento.bpm_global += self.variacao_bpm if self.nota == '>' else self.variacao_bpm * -1

    def character_comando_midi(self) -> MetaMessage:
        self.character_comando()
        return MetaMessage('set_tempo', tempo=bpm2tempo(config_mapeamento.bpm_global), time=0)

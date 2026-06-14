from typing import override
from mido import Message, MidiTrack

from core import config_mapeamento
from core.Icharacter import ICharacter


class CharacterPausa(ICharacter):
    def __init__(self, nota, voz):
        super().__init__(nota, voz)
        self.voz = voz

    @override
    def character_comando(self, track: MidiTrack) -> None:
        track.append(Message('note_off',channel=self.voz.channel, note=self.voz.nota, velocity=0, time=config_mapeamento.PPQ))

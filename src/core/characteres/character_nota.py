from typing import override

from mido import Message, MidiTrack

from core import config_mapeamento
from .Icharacter import ICharacter


class CharacterNota(ICharacter):
    """Tipo de caracter que toca uma nota (e desliga a respectiva nota)"""

    def __init__(self, nota, voz):
        super().__init__(nota, voz)
        self.voz = voz

    @override
    def character_comando(self, track: MidiTrack) -> None:
        track.append(Message("note_on", note=self.voz.nota, channel=self.voz.channel, velocity=self.voz.volume,
                             time=self.voz.delay * config_mapeamento.PPQ))
        track.append(Message("note_off", note=self.nota, channel=self.voz.channel, velocity=0, time=480))

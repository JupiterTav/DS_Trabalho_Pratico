from mido import MidiTrack

from .Icharacter import ICharacter


class CharacterVoz(ICharacter):
    def __init__(self, char, voz):
        super().__init__(char, voz)
        self.voz = voz

    def character_comando(self, track: MidiTrack) -> None:
        if self.nota in '?.':
            self.voz.oitava += 1
        elif self.nota in 'V':
            self.voz.oitava -= 1
        elif self.nota in ' ':
            self.voz.volume *= 2
        return None

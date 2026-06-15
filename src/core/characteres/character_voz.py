from mido import MidiTrack, Message

from .Icharacter import ICharacter


class CharacterVoz(ICharacter):
    """Tipo de character que um parametro na voz"""

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
            track.append(Message('control_change', channel=self.voz.channel, control=7, value=self.voz.volume))
        return None

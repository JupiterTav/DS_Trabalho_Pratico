from typing import override

from mido import Message, MetaMessage, bpm2tempo, MidiTrack

from .track import Track as Voz
from .midi_config import MIDIConfig


class InterpretadorMidi(MIDIConfig):

    @override
    def interpretar_char(self, char: str, *, channel: int, voz: Voz, track: MidiTrack):
        if char in self.notas_midi:
            voz.nota = self.notas_midi[char]

            track.append(self._liga_nota(channel=channel, nota=voz.nota, time=voz.delay))
            track.append(self._desliga_nota(channel=channel, nota=voz.nota))

        elif char in self.gm_intruments:
            voz.instrumento = self.gm_intruments[char]
            track.append(self.troca_instrumento(channel=channel, instrumento=voz.instrumento))

        elif char.isnumeric():
            numero = int(char)
            if (numero % 2) == 0:
                voz.instrumento += numero
                track.append(self.troca_instrumento(channel=channel, instrumento=voz.instrumento))
            else:
                voz.instrumento = 14 # Tubular Bells ou similar fixo
                track.append(self.troca_instrumento(channel=channel, instrumento=voz.instrumento))

        else:
            track.append(self._desliga_nota(channel=channel, nota=voz.nota))

    def is_interpretavel(self, char: str) -> bool:
        if (char in self.notas_midi or 
            char in self.gm_intruments or 
            char in 'abcdefgh' or 
            char.isnumeric()):
            return True
        return False

    def _liga_nota(self, *, channel: int, nota: int, time: int) -> Message:
        return Message('note_on', channel=channel, note=nota, velocity=100, time=time * self._TICKS_PER_BEAT)

    def _desliga_nota(self, *, channel: int, nota: int) -> Message:
        return Message('note_off', channel=channel, note=nota, velocity=0, time=self._TICKS_PER_BEAT)

    def troca_instrumento(self, *, channel: int, instrumento: int) -> Message:
        return Message('program_change', channel=channel, program=instrumento)

    def define_volume(self, *, channel: int,  volume: int) -> Message:
        return Message('control_change', channel=channel, control=7, value=volume)

    def atualiza_bpm(self) -> MetaMessage:
        return MetaMessage('set_tempo', tempo=bpm2tempo(self.bpm_global), time=0)
    def end_of_track(self) -> MetaMessage:
        return MetaMessage('end_of_track', time=0)

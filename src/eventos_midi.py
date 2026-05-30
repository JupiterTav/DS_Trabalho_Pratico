from mido import Message, MetaMessage, bpm2tempo, MidiTrack
from track import Track as Voz
from espec_midi import EspecMidi


class EventosMidi(EspecMidi):

    __TICKS_PER_BEAT = 480

    def interpretaEventoMidi(self, char: str, *, channel: int, voz: Voz, track: MidiTrack):
        if char in self._notas_midi:
            voz.nota = self._notas_midi[char]
            track.append(self.liga_nota(channel=channel, nota=voz.nota_atual, time=voz.delay))
            track.append(self.desliga_nota(voz.nota_atual,channel=channel))

        elif char in self._gm_intruments:
            voz.instrumento = self._gm_intruments[char]
            track.append(self.troca_instrumento(channel=channel, instrumento=voz.instrumento))

        elif char.isnumeric():
            if (int(char) % 2) == 0:
                voz.instrumento += 1
                track.append(self.troca_instrumento(channel=channel, instrumento=voz.instrumento))
            else:
                voz.instrumento = 14
                track.appen(self.troca_instrumento(channel=channel, instrumento=voz.instrumento))

        elif char in 'abcdefgh':
            track.append(self.desliga_nota(channel=channel, nota=voz.nota_atual))

    def liga_nota(self, *, channel: int, nota: str, time: int) -> Message:
        return Message('note_on', channel=channel, note=nota, velocity=100, time=time * self.__TICKS_PER_BEAT)

    def desliga_nota(self, nota, *, channel: int) -> Message:
        return Message('note_off', channel=channel, note=nota, velocity=100, time=self.__TICKS_PER_BEAT)

    def silencia(self, *, channel) -> Message:
        return Message('note_off', channel=channel, time=self.__TICKS_PER_BEAT)

    def troca_instrumento(self, *, channel: int, instrumento) -> Message:
        return Message('program_change', channel=channel, program=instrumento)

    def define_volume(self, *, channel: int,  volume: int):
        return Message('control_change', channel=channel, control=7, value=volume)

    def define_tempo(self, *, bpm: int):
        return MetaMessage('set_tempo', tempo=bpm2tempo(bpm), time=0)

    def end_track(self):
        return MetaMessage('end_of_track', time=0)

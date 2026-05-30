from mido import Message
from track import Track as Voz
from espec_midi import EspecMidi


class EventosMidi(EspecMidi):

    __TICKS_PER_BEAT = 480

    def interpretaEventoMidi(self, char: str, *, channel: int, voz: Voz):
        if char in self._notas_midi:
            voz.nota = self._notas_midi[char]
            return self.liga_nota(channel=channel, nota=voz.nota_atual, time=voz.delay), self.desliga_nota(channel=channel, nota=voz.nota_atual)

        elif char in self._gm_intruments:
            voz.instrumento = self._gm_intruments[char]
            return self.troca_instrumento(channel=channel, instrumento=voz.instrumento)

        elif char.isnumeric():
            if (int(char) % 2) == 0:
                voz.instrumento += 1
                return self.troca_instrumento(channel=channel, instrumento=voz.instrumento)
            else:
                voz.instrumento = 14
                return self.troca_instrumento(channel=channel, instrumento=voz.instrumento)
        elif char in 'abcdefgh':
            return self.desliga_nota(channel=channel, nota=voz.nota_atual)

    def liga_nota(self, *, channel: int, nota: str, time: int) -> Message:
        msg = Message('note_on', channel=channel, note=nota, velocity=100, time=time * self.__TICKS_PER_BEAT)
        return msg

    def desliga_nota(self, *, channel: int, nota) -> Message:
        msg = Message('note_off', channel=channel, note=nota, velocity=100, time=self.__TICKS_PER_BEAT)
        return msg

    def troca_instrumento(self, *, channel: int, instrumento) -> Message:
        msg = Message('program_change', channel=channel, program=instrumento)
        return msg

    def define_volume(self, *, channel: int,  volume: int):
        return Message('control_change', channel=channel, control=7, value=volume)

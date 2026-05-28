from mido import Message
from track import Track as Voz


class EventosMidi:

    __TICKS_PER_BEAT = 480

    def liga_nota(self,  *, channel: int, voz=Voz()) -> Message:
        return Message('note_on', channel=channel, note=voz.nota_atual, velocity=100, time=voz.delay * self.__TICKS_PER_BEAT)

    def desliga_nota(self, *, channel: int, voz=Voz()) -> Message:
        return Message('note_off', channel=channel, note=voz.nota_atual, velocity=100, time=self.__TICKS_PER_BEAT)

    def troca_instrumento(channel: int, voz=Voz()) -> Message:
        return Message('program_change', channel=channel, program=voz.instrumento)


from mido import Message
from track import Track as Voz
from espec_midi import EspecMidi


class EventosMidi(EspecMidi):

    __TICKS_PER_BEAT = 480

    def liga_nota(self,  *, channel: int, nota, time) -> Message:
        return Message('note_on', channel=channel, note=self._notas_midi[nota], velocity=100, time=time * self.__TICKS_PER_BEAT)

    def desliga_nota(self, *, channel: int, nota) -> Message:
        return Message('note_off', channel=channel, note=self._notas_midi[nota], velocity=100, time=self.__TICKS_PER_BEAT)

    def troca_instrumento(self, channel: int, instrumento) -> Message:
        return Message('program_change', channel=channel, program=self._gm_intruments[instrumento])


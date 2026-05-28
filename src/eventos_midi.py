from mido import Message, MidiTrack
from track import Track


class EventosMidi:

    __TICKS_PER_BEAT = 480

    def liga_nota(self,  *, channel: int, track=Track()) -> Message:
        return Message('note_on', channel=channel, note=track.nota_atual, velocity=100, time=track.delay * self.__TICKS_PER_BEAT)

    def desliga_nota(self, *, channel: int, track=Track()) -> Message:
        return Message('note_off', channel=channel, note=track.nota_atual, velocity=100, time=self.__TICKS_PER_BEAT)

    def troca_instrumento(channel: int, track=Track()) -> Message:
        return Message('program_change', channel=channel, program=track.instrumento)


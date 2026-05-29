import os
from mido import Message, MidiTrack, MidiFile
from espec_midi import EspecMidi


class GerenciadorMidi(EspecMidi):

    __TICKS_PER_BEAT = 480

    def __init__(self):
        super.__init__()

        self.__arq_midi = MidiFile(type=1, ticks_per_beat=480)
        self.__caminho = ""

    def gerarArquivo(self, caminho: str):
        try:
            os.makedirs(os.path.dirname(caminho), exist_ok=True)

            if ".midi" or ".mid" not in caminho:
                self.__caminho = caminho + ".mid"
            else:
                self.__caminho = caminho

            self.__arq_midi.save(self.__caminho)

        except OSError as e:
            print(f"Ocorreu um erro no sistema, {e}")
        except PermissionError:
            print("Permissão negada para criação do arquivo")
        return 0



    def liga_nota(self,  *, channel: int, nota, time) -> Message:
        return Message('note_on', channel=channel, note=self._notas_midi[nota], velocity=100, time=time * self.__TICKS_PER_BEAT)

    def desliga_nota(self, *, channel: int, nota) -> Message:
        return Message('note_off', channel=channel, note=self._notas_midi[nota], velocity=100, time=self.__TICKS_PER_BEAT)

    def troca_instrumento(self, channel: int, instrumento) -> Message:
        return Message('program_change', channel=channel, program=self._gm_intruments[instrumento])


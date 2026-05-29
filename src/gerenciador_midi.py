import os
from mido import Message, MidiTrack, MidiFile
from espec_midi import EspecMidi


class GerenciadorMidi(EspecMidi):

    __TICKS_PER_BEAT = 480

    def __init__(self):
        super().__init__()

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

    def criaTrack(self, *, track_name: str):
        track = MidiTrack()
        self.__arq_midi.tracks.append(track)
        track.name = track_name

        self.__arq_midi.save(self.__caminho)

        return track

    def salvaArquivo(self):
        self.__arq_midi.save(self.__caminho)

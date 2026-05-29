import os
from mido import Message, MidiTrack, MidiFile
from espec_midi import EspecMidi


class GerenciadorMidi(EspecMidi):
    def __init__(self):
        self.__arq_midi = MidiFile(type=1, ticks_per_beat=480)
        self.__caminho = ""

    def gerarArquivo(self, caminho: str):
        os.makedirs(os.path.dirname(caminho), exist_ok=True)

        if ".midi" or ".mid" not in caminho:
            self.__caminho = caminho + ".mid"
        else:
            self.__caminho = caminho

        self.__arq_midi.save(self.__caminho)


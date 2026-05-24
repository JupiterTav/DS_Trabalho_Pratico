import os
from interpretador import Interpretador
from gerenciadorVozes import GerenciadorVozes


class GerenciadorArquivoMidi:

    def __init__(self):
        self.midiFile = ""

    def criarArquivo(self, caminho, vozes: GerenciadorVozes()):
        if os.path.exists(caminho):
            print("{} já existe. Deletando...", caminho)
            os.remove("caminho")

        os.makedirs(os.path.dirname(caminho), exist_ok=True)
        if (".midi" or ".mid") in caminho:
            self.midiFile = open(caminho, "w")
        else:
            self.midiFile = open(caminho + ".mid", "w")

        self.__escreveHeaderChunck__(vozes)
        self.midiFile.close()

    def __escreveHeaderChunk__(self, vozes: GerenciadorVozes()):
        with open(self.midiFile.name, 'a'):
            header_label = "4d 54 68 64"  # MThd
            headerLength = vozes.len_vozes()
            self.midiFile.write(
                    f"{header_label} 00 00 00 06 00 02 00 0{headerLength} 00 60")

    def __escreveTrackChunk__(self, vozes: GerenciadorVozes(), _interpreador: Interpretador()):
        track_label = "4d 54 72 6b"  # MTrk
        with open(self.midiFile.name, 'a'):
            for voz in vozes.get_vozes():
                self.midiFile.write(f" {track_label} ")

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

        self.__escreveHeaderChunk__(vozes)
        self.__escreveTrackChunk__(vozes)

    def __escreveHeaderChunk__(self, vozes: GerenciadorVozes()):
        with open(self.midiFile.name, 'a'):
            header_label = "4d 54 68 64"  # MThd
            headerLength = vozes.len_vozes()
            self.midiFile.write(
                    f"{header_label} 00 00 00 06 00 02 00 0{headerLength} 00 60")

    def __escreveTrackChunk__(self, vozes= GerenciadorVozes(), _interpretador= Interpretador()):
        track_label = "4d 54 72 6b"  # MTrk
        with open(self.midiFile.name, 'a'):
            for voz in vozes.get_vozes():
                if '[' and ']' in voz.voz_texto and voz.voz_texto[0] == '[':
                    close_bracket_index = voz.voz_texto.index(']')
                    voz.set_atraso(int(voz.voz_texto[1:close_bracket_index]))
                self.midiFile.write(f" {track_label} 00 00 00 8c 0{voz.get_atraso():x} ff 2f 00")
            self.midiFile.close()

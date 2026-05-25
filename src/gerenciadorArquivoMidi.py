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
        midi_event = ""
        end_track = "ff 2f 00"
        with open(self.midiFile.name, 'a'):
            for i,voz in enumerate(vozes.get_vozes()):
                inicio = 0
                if '[' and ']' in voz.voz_texto and voz.voz_texto[0] == '[':
                    close_bracket_index = voz.voz_texto.index(']')
                    inicio = close_bracket_index + 1 
                    voz.set_atraso(int(voz.voz_texto[1:close_bracket_index]))
                for j in range(inicio, len(voz.voz_texto)):
                    if voz.voz_texto[j] in _interpretador.notas_midi:
                        midi_event += f" 9{i} {voz.get_volume():x} {_interpretador.notas_midi[voz.voz_texto[j]]} 81 00 8{i} 00 {_interpretador.notas_midi[voz.voz_texto[j]]} "
                self.midiFile.write(f" {track_label} 00 00 00 8c {voz.get_atraso():x} {midi_event} {end_track}")
            self.midiFile.close()

    def __escreveEvent__(self, inicio, voz_texto="", _interpretador=Interpretador()):
        for i in range(inicio, len(voz_texto)):
            if voz_texto[i] in _interpretador.notas_midi:
                self.midiFile.write(" 00")



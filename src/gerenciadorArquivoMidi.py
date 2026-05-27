import os
from mido import Message, MidiTrack, MidiFile
from interpretador import Interpretador
from gerenciadorVozes import GerenciadorVozes


class GerenciadorArquivoMidi:

    def __init__(self):
        self.midiFile = MidiFile(type=1, ticks_per_beat=480)
        self.caminho = ""

    def criarArquivo(self, caminho, vozes: GerenciadorVozes()):
        self.caminho = caminho
        os.makedirs(os.path.dirname(caminho), exist_ok=True)

        if (".midi" or ".mid") not in caminho:
            self.caminho = caminho+'.mid'

            self.midiFile.save(caminho)

        self.__escreveTrackChunk__(vozes)

    def __escreveTrackChunk__(self, vozes=GerenciadorVozes()):

        _interpretador = Interpretador()

        for i, voz in enumerate(vozes.get_vozes()):
            track = MidiTrack()
            self.midiFile.tracks.append(track)
            track.name = f'voz {i}'
            track.append(Message('control_change', channel=i, control=7, value=voz.get_volume()))
            """
                DELAY - NOTE_ON - NOTE_OFF
            """
            inicio = 0
            if '[' and ']' in voz.voz_texto and voz.voz_texto[0] == '[':
                close_bracket_index = voz.voz_texto.index(']')
                inicio = close_bracket_index + 1
                voz.set_atraso(int(voz.voz_texto[1:close_bracket_index]))
            for j in range(inicio, len(voz.voz_texto)):
                if voz.voz_texto[j] in _interpretador.notas_midi:
                    track.append(Message('note_on', channel=i, note=_interpretador.notas_midi[voz.voz_texto[j]]+(12*voz.get_oitava()), 
                                            velocity=100, time=voz.get_atraso()*self.midiFile.ticks_per_beat))
                    track.append(Message('note_off', channel=i,note=_interpretador.notas_midi[voz.voz_texto[j]]+(12*voz.get_oitava()), 
                                            velocity=100,time=480))

                elif voz.voz_texto[j] in _interpretador.gm_intruments_comando:
                    voz.set_instrumento(_interpretador.gm_intruments_comando[voz.voz_texto[j]])
                    track.append(Message('program_change', channel=i, program=voz.get_instrumento(), time=0))

                elif voz.voz_texto[j].isnumeric():
                    if (int(voz.voz_texto[j]) % 2) == 0:
                        voz.set_instrumento(voz.get_instrumento() + 1)
                        track.append(Message('program_change', channel=i, program=voz.get_instrumento(), time=0))
                    else:
                        voz.set_instrumento(14)
                        track.append(Message('program_change', channel=i, program=voz.get_instrumento(), time=0))
                elif voz.voz_texto[j] in '?.':
                    voz.set_oitava(voz.get_oitava()+1)

                elif voz.voz_texto[j] == 'V':
                    voz.set_oitava(voz.get_oitava()-1)

                elif voz.voz_texto[j] in 'abcdefgh':
                    track.append(Message('note_off', channel=i, time=480))
                elif voz.voz_texto[j] == ' ':
                    voz.dobra_volume()
                elif voz.voz_texto[j] == '>':
                    vozes.bpm_global = vozes.bpm_global+10
                elif voz.voz_texto[j] == '<':
                    vozes.bpm_global = vozes.bpm_global-10
                else:
                    if voz.voz_texto[j-1] in _interpretador.notas_midi:
                        tracks.append(Message('note_on', channel=i, note=_interpretador.notas_midi[voz.voz_texto[j]]+(12*voz.get_oitava()),
                                                velocity=100, time=voz.get_atraso()*self.midiFile.ticks_per_beat))
                        track.append(Message('note_off', channel=i,note=_interpretador.notas_midi[voz.voz_texto[j]]+(12*voz.get_oitava()),
                                                velocity=100, time=480))
                    else:
                        track.append(Message('note_off', channel=i, time=480))
            self.midiFile.save(self.caminho)

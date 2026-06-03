import os
from typing import  override
from mido import  MetaMessage, MidiTrack, MidiFile

from core.Igerenciador_arquivo import IGerenciador_arquivo
from core.track import Track
from core.eventos_midi import EventosMidi


class GerenciadorMidi(IGerenciador_arquivo):

    def __init__(self):

        self.__evento_midi = EventosMidi()
        self.__arq_midi = MidiFile(type=1, ticks_per_beat=480)
        self.__caminho: str = ""

    @override
    def criar_arquivo(self, caminho: str) -> int:
        try:
            
            self.__caminho = caminho + ".mid"
            if os.path.exists(self.__caminho):
                os.remove(self.caminho)
            self.__arq_midi.save(self.__caminho)

        except OSError as e:
            print(f"Ocorreu um erro no sistema, {e}")
            return -1

        return 0

    @override
    def processar_arquivo(self, vozes: list[Track]):
        for i, voz in enumerate(vozes):
            track = self.criaTrack(track_name=f'voz {i}')

            track.append(MetaMessage('text', text=f'Melodia da voz {i}', time=0))
            track.append(self.__evento_midi.define_volume(channel=i, volume=voz.volume))
            track.append(self.__evento_midi.atualiza_bpm())

            for j, char in enumerate(voz.texto_track):
                if char == (self.__evento_midi.notas_midi.keys() or self.__evento_midi.gm_intruments.keys() or 'abcdefgh' or char.isnumeric()):
                    self.__evento_midi.interpretaEventoMidi(voz.texto_track[j], channel=i, voz=voz, track=track)

                elif char in '?.':
                    voz.oitava += 1
                elif char in 'V':
                    voz.oitava -= 1
                elif char in '>':
                    self.__evento_midi.bpm_global += 10
                    track.append(self.__evento_midi.atualiza_bpm())
                elif char in '<':
                    self.__evento_midi.bpm_global -= 10
                    track.append(self.__evento_midi.atualiza_bpm())
                elif char in ' ':
                    voz.volume *= 2
                    track.append(self.__evento_midi.define_volume(channel=i, volume=voz.volume))

                else:
                    if voz.texto_track[j-1] in self.__evento_midi.notas_midi:
                        self.__evento_midi.interpretaEventoMidi(voz.texto_track[j-1], channel=i, voz=voz, track=track)
                    else:
                        self.__evento_midi.interpretaEventoMidi(voz.texto_track[j], channel=i, voz=voz, track=track)
            track.append(self.__evento_midi.end_of_track())


    def criaTrack(self, *, track_name: str) -> MidiTrack:
        track = MidiTrack()
        self.__arq_midi.tracks.append(track)
        track.name = track_name

        self.__arq_midi.save(self.__caminho)

        return track

    @override
    def salvar_arquivo(self):
        self.__arq_midi.save(filename=self.__caminho)
    
    @property
    def caminho(self) -> str:
        if not os.path.exists(self.__caminho):
            raise FileNotFoundError(f'{self.__caminho} não encontrado')
        return self.__caminho

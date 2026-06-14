import os
from typing import  override
from mido import  MetaMessage, MidiTrack, MidiFile

from core.Igerenciador_arquivo import IGerenciador_arquivo
from core.voz import Voz
from core.interpretador_midi import InterpretadorMidi


class GerenciadorMidi(IGerenciador_arquivo):

    def __init__(self):

        self.__evento_midi = InterpretadorMidi()
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
    def processar_arquivo(self, vozes: list[Voz]):
        for i, voz in enumerate(vozes):
            track = self.criaTrack(track_name=f'voz {i}')

            track.append(MetaMessage('text', text=f'Melodia da voz {i}', time=0))
            track.append(self.__evento_midi.define_volume(channel=voz.channel, volume=voz.volume))
            track.append(self.__evento_midi.troca_instrumento(channel=voz.channel, instrumento=voz.instrumento))
            track.append(self.__evento_midi.atualiza_bpm())
#            ultima_nota = ""
            j = 0
            texto = voz.texto_track
            while j < len(texto):
                print("interpretando character ", j)
                voz.characteres[j].character_comando(track)
                print("instrumento ", voz.instrumento)
                print("oitava", voz.oitava)
                print("foi interpretado character ", j)
                j += 1

            #track.append(self.__evento_midi.end_of_track())


    def criaTrack(self, *, track_name: str) -> MidiTrack:
        track = MidiTrack()
        self.__arq_midi.tracks.append(track)
        track.name = track_name

        self.__arq_midi.save(self.__caminho)

        return track

    @override
    def salvar_arquivo(self):
        self.__arq_midi.save(filename=self.__caminho)

    def set_bpm(self, bpm: int):
        self.__evento_midi.bpm_global = bpm
    
    @property
    def caminho(self) -> str:
        if not os.path.exists(self.__caminho):
            raise FileNotFoundError(f'{self.__caminho} não encontrado')
        return self.__caminho

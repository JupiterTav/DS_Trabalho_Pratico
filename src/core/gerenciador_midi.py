import os
from typing import  override
from mido import  MetaMessage, MidiTrack, MidiFile

from core.Igerenciador_arquivo import IGerenciador_arquivo
from core.track import Track
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
    def processar_arquivo(self, vozes: list[Track]):
        for i, voz in enumerate(vozes):
            track = self.criaTrack(track_name=f'voz {i}')

            track.append(MetaMessage('text', text=f'Melodia da voz {i}', time=0))
            track.append(self.__evento_midi.define_volume(channel=i, volume=voz.volume))
            track.append(self.__evento_midi.troca_instrumento(channel=i, instrumento=voz.instrumento))
            track.append(self.__evento_midi.atualiza_bpm())
            ultima_nota = ""
            j = 0
            texto = voz.texto_track
            while j < len(texto):
                char = texto[j]

                # Suporte a Bemol (Ex: Eb, Ab)
                if char in "ABCDEFG" and j + 1 < len(texto) and texto[j+1] == 'b':
                    char = char + 'b'
                    j += 1

                # 1. Se for uma NOTA
                if char in self.__evento_midi.notas_midi:
                    ultima_nota = char
                    self.__evento_midi.interpretar_char(char, channel=i, voz=voz, track=track)

                # 2. Se for uma PAUSA explícita (a-h minúsculas)
                elif char in 'abcdefgh':
                    ultima_nota = ""
                    self.__evento_midi.interpretar_char("", channel=i, voz=voz, track=track)

                # 3. Comandos que NÃO são notas (Limpam a memória de repetição)
                elif char in self.__evento_midi.gm_intruments or char.isnumeric():
                    ultima_nota = ""
                    self.__evento_midi.interpretar_char(char, channel=i, voz=voz, track=track)

                elif char in '?.':
                    voz.oitava += 1
                    ultima_nota = ""
                elif char in 'V':
                    voz.oitava -= 1
                    ultima_nota = ""
                elif char in '>':
                    self.__evento_midi.bpm_global += 10
                    track.append(self.__evento_midi.atualiza_bpm())
                    ultima_nota = ""
                elif char in '<':
                    self.__evento_midi.bpm_global -= 10
                    track.append(self.__evento_midi.atualiza_bpm())
                    ultima_nota = ""
                elif char in ' ':
                    voz.volume *= 2
                    track.append(self.__evento_midi.define_volume(channel=i, volume=voz.volume))
                    ultima_nota = ""

                # 4. Caracteres não classificados (X, Y, Z, consoantes, etc.)
                else:
                    # Se o anterior era nota, REPETE (Trinado)
                    # Se não era nota, PAUSA
                    self.__evento_midi.interpretar_char(ultima_nota, channel=i, voz=voz, track=track)
                
                j += 1
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

    def set_bpm(self, bpm: int):
        self.__evento_midi.bpm_global = bpm
    
    @property
    def caminho(self) -> str:
        if not os.path.exists(self.__caminho):
            raise FileNotFoundError(f'{self.__caminho} não encontrado')
        return self.__caminho

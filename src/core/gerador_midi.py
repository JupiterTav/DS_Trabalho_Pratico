import os
from typing import override

from mido import Message, MidiTrack, MidiFile

from core.Igerador_arquivo import IGerador_arquivo


class GeradorMidi(IGerador_arquivo):
    """Comanda métodos para criar um arquivo midi"""

    def __init__(self):
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

    def cria_track(self, *, track_name: str, channel, volume_inicial, instrumento_inicial) -> MidiTrack:
        """Cria Track Doc: Anexa ao arquivo e retorna uma Midi Track
        com volume e intrumento inicial como eventos default
        """
        track = MidiTrack()
        self.__arq_midi.tracks.append(track)
        track.name = track_name

        track.append(Message('control_change', channel=channel, control=7, value=volume_inicial))
        track.append(Message('program_change', channel=channel, program=instrumento_inicial))

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

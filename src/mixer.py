import pathlib

import pygame

from enum import Enum

from core.io_manager import IOManager
from core.conversor import Conversor
from core.gerenciador_midi import GerenciadorMidi
from core.track import Track
from ui.campo_editavel import CampoEditavel 

class MixerState(Enum):
    EDITING = 0
    GENERATING = 1
    SYNTHESIZING = 2
    PLAYING = 3
    QUIT = 4

class Mixer:
    paused: bool

    def __init__(self) -> None:
        self.__arq_output = None
        self.state = MixerState.EDITING
        pygame.mixer.init()
        self.editing()
        self.loaded = False


    def editing(self):
        self.state = MixerState.EDITING
        print("[MIXER] EDITING")

        self.__arq_midi: GerenciadorMidi = GerenciadorMidi()
        self.__vozes: list[Track] = []
        self.__arq_output: str = ""

        self.paused = False

    def start(self, list_campo: list[CampoEditavel]):
        try:
            filepath = IOManager.get_output_path()

            for  campo in list_campo:
                voz = Track(campo.campo_texto.get(), 
                          int(campo.param_volume.get()), int((campo.param_oitava.get())))
                self.__vozes.append(voz)

            self.generate(filepath)
        except ValueError:
            print("[Mixer] Erro ao inicializar")

    def generate(self, filepath: pathlib.Path):
        try:
            self.state = MixerState.GENERATING
            print("[MIXER] GENERATING")

            self.__arq_output = str(filepath)
            self.__arq_midi.criar_arquivo(str(filepath.with_suffix('')))

            self.__arq_midi.processar_arquivo(vozes=self.__vozes)
            self.__arq_midi.salvar_arquivo()

            self.synth()
        except ValueError:
            print(f"[Mixer] Erro ao Gerar o arquivo!\n")

    def synth(self):
        try: 
            self.state = MixerState.SYNTHESIZING
            print("[MIXER] SYNTHESIZING")

            conversor = Conversor("assets/TimGM6mb.sf2")
            _ = conversor.converter_midi_audio(input_path=self.__arq_midi.caminho, 
                                           output_path=self.__arq_output, volume=100)
            if _:
                self.play_track()
        except ValueError:
            print(f"[MIXER] Erro ao sintetizar!")

    def play_track(self):
        self.state = MixerState.PLAYING

        print("[MIXER] PLAYING")
        try:
            pygame.mixer.music.load(self.__arq_output)
            self.loaded = True

            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(0.7)

            self.editing()
        except:
            print(f"[Mixer] Erro ao tocar")

    def on_pause(self):
        if self.loaded:
            if self.paused:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.pause()
            self.paused = not self.paused
    def on_play(self):
        if self.loaded:
            if self.paused:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.rewind()
                pygame.mixer.music.play()

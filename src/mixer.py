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
    def __init__(self) -> None:
        pygame.mixer.init()
        self.editing()
        self.loaded = False


    def editing(self):
        self.state: MixerState = MixerState.EDITING 
        print("[MIXER] EDITING") 
        self.__arq_midi: GerenciadorMidi = GerenciadorMidi()
        self.__vozes: list[Track] = []
        self.__arq_output: str = ""

        self.paused = False


    def start(self, list_campo: list[CampoEditavel]):
        self.state = MixerState.GENERATING
        print("[MIXER] GENERATING") 
        try: 
            
            filepath = IOManager.get_output_path()
            print(list_campo)

            for  i,campo in enumerate(list_campo):
                print(f'campo {i}: {campo.campo_texto.get()}\n')
                voz = Track(campo.campo_texto.get(), 
                          int(campo.param_volume.get()), int((campo.param_oitava.get())))
                self.__vozes.append(voz)

            self.__arq_output = str(filepath)

            _ = self.__arq_midi.criar_arquivo(str(filepath.with_suffix('')))
            self.__arq_midi.processar_arquivo(vozes=self.__vozes)
            self.__arq_midi.salvar_arquivo()
            
            print(self.__vozes)

            self.synth()
        except ValueError:
            print(f"[Mixer] Erro Ao Generar o arquivo!\n ")
    
    def synth(self):
        try: 
            self.state = MixerState.SYNTHESIZING
            print("[MIXER] SYNTHESIZING")

            conversor = Conversor("assets/TimGM6mb.sf2")
            _ = conversor.converter_midi_audio(input_path=self.__arq_midi.caminho, 
                                           output_path=self.__arq_output, volume=100)
            if _ == True:
                self.play_track()
        except ValueError:
            print(f"[MIXER] Erro ao sintetizar!")

    def play_track(self):
        self.state = MixerState.PLAYING
        print("[MIXER] PLAYING") 
        pygame.mixer.music.load(self.__arq_output)
        self.loaded = True 
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(0.7)
        self.state = MixerState.EDITING
        self.editing()

    def on_pause(self):
        if self.loaded == True: 
            if self.paused == False:
                pygame.mixer.music.pause()
                self.paused = True
            else:
                pygame.mixer.music.unpause()
                self.paused = False
    def on_play(self):
        if self.loaded == True:
            if self.paused == False:
                pygame.mixer.music.rewind()
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.unpause()

import pathlib
import pygame

from enum import Enum

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

        self.state = MixerState.EDITING 
        self.__arq_midi: GerenciadorMidi = GerenciadorMidi()
        self.__vozes: list[Track] = []
        self.__arq_output: str = ""


    def start(self, list_campo: list[CampoEditavel], filepath: pathlib.Path):
        self.state = MixerState.GENERATING
        try: 
            
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

            pygame.mixer.init()

            conversor = Conversor("assets/TimGM6mb.sf2")
            _ = conversor.converter_midi_audio(input_path=self.__arq_midi.caminho, 
                                           output_path=self.__arq_output, volume=100)
            if _ == True:
                self.play()
        except ValueError:
            print(f"[MIXER] Erro ao sintetizar!")

    def play(self):
        self.state = MixerState.PLAYING
        
        pygame.mixer.music.load(self.__arq_output)
        pygame.mixer.music.play(1)
        pygame.mixer.music.set_volume(1.0)
        
        self.state = MixerState.EDITING


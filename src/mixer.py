from enum import Enum

from core.gerador_vozes import GeradorVozes
from core.gerenciador_midi import GerenciadorMidi
from core.track import Track

from core.voz import Voz
from ui.campo_editavel import CampoEditavel 

class MixerState(Enum):
    GENERATING = 0
    SYNTHESIZING = 1
    PLAYING = 2 
    INACTIVE = 3

class Mixer:
    def __init__(self) -> None:
        self.state = MixerState.INACTIVE
        self.__gerador_vozes: GeradorVozes = GeradorVozes()
        self.__arq_midi: GerenciadorMidi = GerenciadorMidi()
        self.__vozes: list[Track] = []

    def start(self, list_campo: list[CampoEditavel], filepath: str):
        self.state = MixerState.GENERATING
        try: 
            for  campo in list_campo:
                voz = Voz(campo.campo_texto.get(), int(campo.param_volume.get()), int((campo.param_oitava.get())))
                self.__vozes.append(voz)

            _ = self.__arq_midi.criar_arquivo(filepath)
            self.__arq_midi.processar_arquivo(vozes=self.__vozes, global_vozes=self.__gerador_vozes)
            self.__arq_midi.salvar_arquivo

            self.state = MixerState.SYNTHESIZING
        except ValueError as e:
            print(f"Erro!\n {e}")


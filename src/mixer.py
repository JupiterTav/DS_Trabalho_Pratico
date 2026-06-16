from enum import Enum

import pygame

from core.conversor import Conversor
from core.gerador_midi import GeradorMidi
from core.io_manager import IOManager
from core.voz import Voz
from ui.campo_texto_editavel import CampoTextoEditavel


class MixerState(Enum):
    EDITING = 0
    GENERATING = 1
    SYNTHESIZING = 2
    PLAYING = 3


class Mixer:
    """Responsaavel pelo pipeline do arquivo de som e "mediador" dos módulos de core e UI.
        Dividimos o pipeline em:
            EDITING -> Escrevendo o texto nos campos da UI;
            GENERATING -> Gera o arquivo midi a partir das vozes e dados extraidos dos campos;
            SYNTHESIZING -> Sintetiza o output de generating em um arquivo de som;
            PLAYING -> Toca o arquivo de som (output de synthesizing).
    """
    paused: bool

    def __init__(self) -> None:
        self.__vozes = None
        self.__arq_midi = None
        self.__arq_output = ""
        self.state = MixerState.EDITING
        pygame.mixer.init()
        self.editing()

    def editing(self):
        self.state = MixerState.EDITING
        print("[MIXER] EDITING")

        self.__arq_midi: GeradorMidi = GeradorMidi()
        self.__vozes: list[Voz] = []

        self.paused = False

    def start(self, list_campo: list[CampoTextoEditavel], on_finish=None, on_error=None):
        try:

            self.__vozes = []
            for i, campo in enumerate(list_campo):
                voz = Voz(campo.campo_texto.get(),
                          int(campo.param_volume.get()), int((campo.param_oitava.get())), channel=i)
                try:
                    instrumento = int(campo.param_instrumento.get())
                    voz.instrumento = instrumento
                except (ValueError, Exception):
                    voz.instrumento = 0  # Fallback para piano se der erro

                self.__vozes.append(voz)

            self.generate()

            if on_finish:
                on_finish()

        except Exception as e:
            print(f"[Mixer] Erro ao inicializar: {e}")

            if on_error:
                on_error(str(e))

    def generate(self):
        try:
            self.state = MixerState.GENERATING
            print("[MIXER] GENERATING")

            filepath = IOManager.get_output_path()

            self.__arq_output = str(filepath)
            self.__arq_midi.criar_arquivo(str(filepath.with_suffix('')))

            for i, voz in enumerate(self.__vozes):
                atual_track = self.__arq_midi.cria_track(track_name=f"Track {i}", channel=voz.channel,
                                                         volume_inicial=voz.volume,
                                                         instrumento_inicial=voz.instrumento)
                j = 0
                while j < len(voz.texto_track):
                    char = voz.texto_track[j]
                    if j + 1 < len(voz.texto_track) and char in 'ABCDEFG' and voz.texto_track[j + 1] == 'b':
                        char = char + 'b'
                        j += 1
                    voz.interpretar(char).character_comando(atual_track)
                    j += 1
                self.__arq_midi.salvar_arquivo()

            self.__arq_midi.salvar_arquivo()

            self.synth()
        except ValueError:
            print(f"[Mixer] Erro ao Gerar o arquivo!\n")

    def synth(self):
        try:
            self.state = MixerState.SYNTHESIZING
            print("[MIXER] SYNTHESIZING")

            import pathlib
            base_dir = pathlib.Path(__file__).parent.parent.resolve()
            sf2_path = base_dir / "assets" / "TimGM6mb.sf2"
            conversor = Conversor(str(sf2_path))
            _ = conversor.converter_midi_audio(input_path=self.__arq_midi.caminho,
                                               output_path=self.__arq_output,
                                               volume=100)  # Todo: volume configuravel pela interface
            if _:
                self.play_track()
        except ValueError:
            print(f"[MIXER] Erro ao sintetizar!")

    def play_track(self):
        self.state = MixerState.PLAYING

        print("[MIXER] PLAYING")
        try:
            pygame.mixer.music.load(self.__arq_output)

            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(1)

            self.editing()
        except ValueError:
            print(f"[Mixer] Erro ao tocar")

    def on_pause(self):
        if self.paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        self.paused = not self.paused

    def on_play(self):
        if self.paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.rewind()
            pygame.mixer.music.play()

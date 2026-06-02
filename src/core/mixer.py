from enum import Enum
import os

from core.gerador_vozes import GeradorVozes
from core.gerenciador_midi import GerenciadorMidi
from core.conversor import Conversor

class MixerState(Enum):
    EDITING = 0
    GENERATING = 1
    SYNTHESIZING = 3
    PLAYING = 4
    QUIT = 5

class Mixer:
    def __init__(self):
        self.estado = MixerState.EDITING
        self.build_dir = "build"
        
        # Garante que o diretório de destino exista (regra de negócio)
        if not os.path.exists(self.build_dir):
            os.makedirs(self.build_dir)
            
        self.conversor = Conversor("assets/TimGM6mb.sf2")
        self.arquivo_midi = GerenciadorMidi()
        self.gerador_vozes = GeradorVozes()
        
        self.linhas = []
        self.vozes = []
        
    def iniciar_geracao(self, linhas):
        """Inicia a geração de áudio a partir das linhas de texto."""
        if self.estado in (MixerState.EDITING, MixerState.QUIT):
            self.linhas = linhas
            self.estado = MixerState.GENERATING
            print("[Mixer] Iniciando geração...")
            
    def processar_estado(self):
        """
        Avança um passo na máquina de estados. 
        Deve ser chamado periodicamente pela UI (ex: via after).
        """
        if self.estado == MixerState.GENERATING:
            print("[Mixer] Gerando MIDI...")
            self.vozes = self.gerador_vozes.gerar_vozes(self.linhas)
            
            _ = self.arquivo_midi.criar_arquivo(os.path.join(self.build_dir, "saida.mid"))
            self.arquivo_midi.processar_arquivo(self.vozes, self.gerador_vozes)
            self.arquivo_midi.salvar_arquivo()
            
            self.estado = MixerState.SYNTHESIZING
            
        elif self.estado == MixerState.SYNTHESIZING:
            print("[Mixer] Sintetizando Áudio...")
            # TODO: Débito Técnico - A conversão bloqueia a thread atual. 
            # Num futuro próximo, usar threading.Thread aqui para não travar a UI.
            sucesso = self.conversor.converter_midi_audio(
                input_path=self.arquivo_midi.caminho, 
                output_path=os.path.join(self.build_dir, ".wav"), 
                volume=100
            )
            if sucesso:
                self.estado = MixerState.PLAYING
            else:
                self.estado = MixerState.EDITING
                
        elif self.estado == MixerState.PLAYING:
            print("[Mixer] Reproduzindo (Simulação)...")
            # Aqui entraria o código para tocar o áudio com pygame, se desejado.
            self.estado = MixerState.QUIT
            
        elif self.estado == MixerState.QUIT:
            # Retorna ao modo de edição para permitir nova geração
            self.estado = MixerState.EDITING

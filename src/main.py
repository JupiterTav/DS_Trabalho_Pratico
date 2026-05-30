from enum import Enum
from ui.campo_texto import CampoTexto
from core.gerador_vozes import GeradorVozes
from core.gerenciador_midi import GerenciadorMidi

class MixerState(Enum):
    EDITING = 0
    RUNNING = 1
    QUIT = 2

def main():

    texto = CampoTexto()
    estado = MixerState.EDITING
    
    if estado == MixerState.EDITING:
        texto.le_texto()
        estado = MixerState.RUNNING

    if estado == MixerState.RUNNING:
        gerador_vozes = GeradorVozes()
        vozes = gerador_vozes.gerar_vozes(texto.Linhas)
        
        gerenciador_arq = GerenciadorMidi()
        
        _ = gerenciador_arq.criar_arquivo("build/musica")
        gerenciador_arq.processar_arquivo(vozes, gerador_vozes)
        gerenciador_arq.salvar_arquivo()
        
        estado = MixerState.QUIT
        
if __name__ == "__main__":
    main()

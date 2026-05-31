from enum import Enum

from ui.campo_texto import CampoTexto
from core.gerador_vozes import GeradorVozes
from core.gerenciador_midi import GerenciadorMidi
from core.conversor import Conversor

#TODO: Sintezar o arquivo midi que geramos no formato requisitado

class MixerState(Enum):
    EDITING = 0
    GENERATING = 1
    SYNTHETIZING = 3
    QUIT = 4

def main():
    
    conversor = Conversor("/home/tav_wes/Faculdade/DS_Trabalho_Pratico/assets/FluidR3_GM.sf2")

    texto = CampoTexto()
    arquivo_midi = GerenciadorMidi()

    estado = MixerState.EDITING
    
    if estado == MixerState.EDITING:
        texto.le_texto()
        estado = MixerState.GENERATING

    if estado == MixerState.GENERATING:
        gerador_vozes = GeradorVozes()
        vozes = gerador_vozes.gerar_vozes(texto.Linhas)
        
        
        _ = arquivo_midi.criar_arquivo("/home/tav_wes/Faculdade/DS_Trabalho_Pratico/build/musica.mid")
        arquivo_midi.processar_arquivo(vozes, gerador_vozes)
        arquivo_midi.salvar_arquivo()
        estado = MixerState.SYNTHETIZING

    if estado == MixerState.SYNTHETIZING:
        conversor.converter_midi_audio(input_path=arquivo_midi.caminho, output_path="build/main_test.wav", volume=100)
        estado = MixerState.QUIT
        
if __name__ == "__main__":
    main()

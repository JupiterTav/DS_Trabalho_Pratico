from enum import Enum

from ui.campo_texto import CampoTexto
from ui.janela_principal import JanelaPrincipal

from core.gerador_vozes import GeradorVozes
from core.gerenciador_midi import GerenciadorMidi
from core.conversor import Conversor


class MixerState(Enum):
    EDITING = 0
    GENERATING = 1
    SYNTHETIZING = 3
    PLAYING = 4
    QUIT = 5

#TODO: Ao trabalhar na GUI, mover (boa parte) dessa função e o enum acima para uma classe mixer
def main():
    
    conversor = Conversor("assets/TimGM6mb.sf2")
    janela = JanelaPrincipal()

    texto = CampoTexto()
    arquivo_midi = GerenciadorMidi()
    estado = MixerState.EDITING
    
    if estado == MixerState.EDITING:
        texto.le_texto()
        estado = MixerState.GENERATING

    if estado == MixerState.GENERATING:
        gerador_vozes = GeradorVozes()
        vozes = gerador_vozes.gerar_vozes(texto.Linhas)
        
        
        _ = arquivo_midi.criar_arquivo("build/saida.mid")
        arquivo_midi.processar_arquivo(vozes, gerador_vozes)
        arquivo_midi.salvar_arquivo()
        estado = MixerState.SYNTHETIZING

    if estado == MixerState.SYNTHETIZING:
        _ = conversor.converter_midi_audio(input_path=arquivo_midi.caminho, 
                                           output_path="build/.wav", volume=100)
        if _ == True:
            estado = MixerState.PLAYING
    if estado == MixerState.PLAYING:
        estado = MixerState.QUIT

    janela.mainloop()
if __name__ == "__main__":
    main()

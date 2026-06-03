from enum import Enum

from mixer import Mixer
from ui.campo_texto import CampoTexto
from ui.janela_principal import JanelaPrincipal

from core.gerador_vozes import GeradorVozes
from core.gerenciador_midi import GerenciadorMidi
from core.conversor import Conversor


class MixerState(Enum):
    EDITING = 0
    GENERATING = 1
    SYNTHESIZING = 3
    PLAYING = 4
    QUIT = 5

#NOTE: Mixer deve ser o modulo que faz a comunicação entre core e ui.
#NOTE: Main deve majoritamente inicialiar UI e Mixer e suas comunicacoes 

#TODO: Ao trabalhar na GUI, mover (boa parte) dessa função e o enum acima para uma classe mixer
        #TODO: Classe mixer e sua função para inicializar 

def main():
    
    mixer = Mixer()    
    janela = JanelaPrincipal(mixer=mixer)


    janela.mainloop()
if __name__ == "__main__":
    main()

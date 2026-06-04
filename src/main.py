from mixer import Mixer
from ui.janela_principal import JanelaPrincipal

def main():
    
    mixer = Mixer()    
    janela = JanelaPrincipal(mixer=mixer)


    janela.mainloop()
if __name__ == "__main__":
    main()

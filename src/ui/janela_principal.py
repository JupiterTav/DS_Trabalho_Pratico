import customtkinter as ctk

from mixer import Mixer
from ui.reproducao import Reproducao

from .cabecalho import Cabecalho
from .scrollable_campo_texto import ScrollableCampoTexto
from .mixing_button import MixBotao

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class JanelaPrincipal(ctk.CTk):

    def __init__(self, mixer: Mixer):
        super().__init__()
        
        self.title("Sintetizador de texto")
        self.geometry("640x400")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.campo_principal = ScrollableCampoTexto(self)
        self.campo_principal.grid(row=2, column=0, sticky="nsew")

        self.cabecalho = Cabecalho(self, self.campo_principal)
        self.cabecalho.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Função de callback (Mediador) que coordena a ação sem acoplar os componentes
        def ao_clicar_mix(on_finish, on_error):
            bpm_inicial = self.cabecalho.get_bpm()
            lista_campos = self.campo_principal.campos
            
            # Encapsula a finalização para garantir que o play_track seja chamado
            def finalizacao_com_play():
                on_finish()
                mixer.play_track()

            mixer.start(lista_campos, on_finish=finalizacao_com_play, on_error=on_error, bpm_inicial=bpm_inicial)

        self.mix_botao = MixBotao(self, action_callback=ao_clicar_mix)
        self.mix_botao.grid(row=1, column=0, sticky="nsew")

        self.icons_reproducao = Reproducao(self, mixer)
        self.icons_reproducao.grid(row=3, column=0, sticky="nsew", columnspan=3)



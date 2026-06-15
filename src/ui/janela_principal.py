import customtkinter as ctk

from core import config_mapeamento
from mixer import Mixer
from ui.reproducao import Reproducao
from .cabecalho import Cabecalho
from .guia import Guia
from .mixing_button import MixBotao
from .scrollable_campo_texto import ScrollableCampoTexto

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class JanelaPrincipal(ctk.CTk):
    """Janela principal da aplicação. Nela é gerada as componentes da UI e a comunicação com mixer"""

    def __init__(self, mixer: Mixer):
        super().__init__()

        self.title("Sintetizador de texto")
        self.geometry("1024x768")
        self.toplevel_guia = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.campo_principal = ScrollableCampoTexto(self, border_width=2, corner_radius=0)
        self.campo_principal.grid(row=2, column=0, sticky="nsew")

        self.cabecalho = Cabecalho(self, self.campo_principal)
        self.cabecalho.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        def ao_clicar_mix(on_finish, on_error):
            """  Função de callback (Mediador) que coordena a ação sem acoplar os componentes"""
            config_mapeamento.bpm_global = self.cabecalho.get_bpm()
            lista_campos = self.campo_principal.campos

            # Encapsula a finalização para garantir que o play_track seja chamado
            def finalizacao_com_play():
                on_finish()
                mixer.play_track()

            mixer.start(lista_campos, on_finish=finalizacao_com_play, on_error=on_error)

        self.mix_botao = MixBotao(self, action_callback=ao_clicar_mix, height=100)
        self.mix_botao.grid(row=1, column=0, sticky="ew")

        self.icons_reproducao = Reproducao(self, mixer, border_width=0, corner_radius=0)
        self.icons_reproducao.grid(row=3, column=0, sticky="sew", columnspan=3)

        def abre_guia():
            if self.toplevel_guia is None or not self.toplevel_guia.winfo_exists():
                self.toplevel_guia = Guia()
            else:
                self.toplevel_guia.focus()

        self.botao_guia = ctk.CTkButton(self.mix_botao, width=25, height=30, text="📘︎", fg_color="transparent",
                                        font=("Arial", 35), command=abre_guia)
        self.botao_guia.grid(row=0, column=0, sticky="w")

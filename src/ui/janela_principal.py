import customtkinter as ctk

from mixer import Mixer

from .cabecalho import Cabecalho
from .scrollable_campo_texto import ScrollableCampoTexto
from .mixing_button import MixBotao

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

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


        self.mix_botao = MixBotao(self, mixer=mixer, campos_texto=self.campo_principal.campos)
        self.mix_botao.grid(row=1, column=0, sticky="nsew")

        self.row_icons_inferiores = ctk.CTkFrame(self, width=self._current_width, height=20)
        self.row_icons_inferiores.grid(row=3, column=0, sticky="nsew")

        self.row_reproduçao = ctk.CTkFrame(self, width=self._current_width, height=50)
        self.row_reproduçao.grid(row=4, column=0, sticky="nsew")




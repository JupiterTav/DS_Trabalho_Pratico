import customtkinter as ctk

from .cabecalho import Cabecalho
from .baking_button import BakeBotao

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class JanelaPrincipal(ctk.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("Sintetizador de texto")
        self.geometry("640x400")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        ##Row superior 
        self.cabecalho = Cabecalho(self)
        self.cabecalho.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)


        self.bake_botao = BakeBotao(self)
        self.bake_botao.grid(row=1, column=0, sticky="nsew")
        #self.row_icons_superiores.grid(row=1, column=0, sticky="nsew")

        self.row_principal = ctk.CTkScrollableFrame(self, width=self._current_width, height=400)
        self.row_principal.grid(row=2, column=0, sticky="nsew")

        self.row_icons_inferiores = ctk.CTkFrame(self, width=self._current_width, height=20)
        self.row_icons_inferiores.grid(row=3, column=0, sticky="nsew")

        self.row_reproduçao = ctk.CTkFrame(self, width=self._current_width, height=50)
        self.row_reproduçao.grid(row=4, column=0, sticky="nsew")




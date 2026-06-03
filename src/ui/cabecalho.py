import pathlib

import customtkinter as ctk

from core.io_manager import IOManager
from ui.scrollable_campo_texto import ScrollableCampoTexto

class Cabecalho(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, text_area: ScrollableCampoTexto) -> None:
        super().__init__(master)
        
        _ = self.grid_columnconfigure((0), weight=1)

        self.upload_txt: ctk.CTkButton = ctk.CTkButton(self, width=30, height=30, text="↑", corner_radius=70, font=("Arial", 20, "bold"), 
                                                       command=lambda: self.upload_arq_texto(text_area))
        self.upload_txt.grid(row=0, column=0, sticky="w", padx=(0, 10))


    def upload_arq_texto(self, campos_texto: ScrollableCampoTexto):
        txt: pathlib.Path = IOManager.carrega_texto()
        quant_lines = 0
        with open(txt, 'r') as text:
            for line in text:
                campos_texto.campos[quant_lines].campo_texto.insert(0, str(line).replace("\n", ""))
                quant_lines += 1

                if len(campos_texto.campos) < quant_lines+1:
                    campos_texto.adiciona_campo()

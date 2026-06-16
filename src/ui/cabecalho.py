import pathlib
from tkinter import messagebox

import customtkinter as ctk

from core.io_manager import IOManager
from ui.scrollable_campo_texto import ScrollableCampoTexto


class Cabecalho(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, text_area: ScrollableCampoTexto) -> None:
        super().__init__(master)

        _ = self.grid_columnconfigure((0), weight=1)

        self.txt: pathlib.Path = pathlib.Path("")

        self.upload_txt: ctk.CTkButton = ctk.CTkButton(self, width=30, height=30, text="Carregar texto",
                                                       corner_radius=70, font=("Arial", 16, "bold"),
                                                       command=lambda: self.upload_arq_texto(text_area))
        self.upload_txt.grid(row=0, column=0, sticky="w", padx=(0, 10))

        self.download_txt: ctk.CTkButton = ctk.CTkButton(self, width=30, height=30, text="Salvar texto",
                                                         corner_radius=70, font=("Arial", 16, "bold"),
                                                         command=lambda: self.download_text(text_area))
        self.download_txt.grid(row=0, column=0, sticky="e")

        # Campo de BPM Inicial
        self.label_bpm = ctk.CTkLabel(self, text="BPM:", font=("Arial", 14, "bold"))
        self.label_bpm.grid(row=0, column=0, padx=(200, 0), sticky="w")

        self.campo_bpm = ctk.CTkEntry(self, width=50, height=30, corner_radius=5)
        self.campo_bpm.insert(0, "120")
        self.campo_bpm.grid(row=0, column=0, padx=(250, 0), sticky="w")

    def get_bpm(self) -> int:
        try:
            bpm = int(self.campo_bpm.get())
            return bpm if bpm > 0 else 120
        except ValueError:
            return 120

    def upload_arq_texto(self, campos_texto: ScrollableCampoTexto):
        self.txt: pathlib.Path = IOManager.carrega_texto()
        if str(self.txt) == "" or str(self.txt) == ".": # canceled dialog
            return

        # Limpar campos existentes
        for campo in campos_texto.campos:
            campo.campo_texto.delete(0, "end")

        quant_lines = 0
        with open(self.txt, 'r') as text:
            for line in text:
                if len(campos_texto.campos) < quant_lines + 1:
                    campos_texto.adiciona_campo()
                
                campos_texto.campos[quant_lines].campo_texto.delete(0, "end")
                campos_texto.campos[quant_lines].campo_texto.insert(0, str(line).replace("\n", ""))
                quant_lines += 1

    def download_text(self, campos_texto: ScrollableCampoTexto):
        try:
            if not self.txt.is_file():
                self.txt = IOManager.salvar_arq()
            with open(self.txt, 'w') as text:
                for campo in campos_texto.campos:
                    text.write(campo.campo_texto.get() + '\n')
            messagebox.showinfo("Sucesso!", message="Texto Salvo")
        except:
            messagebox.showerror("Arquivo não carregado!", message="Carregue o arquivo texto antes de salvar")

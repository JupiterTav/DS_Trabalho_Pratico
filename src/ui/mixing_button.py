import customtkinter as ctk

from tkinter import filedialog

from mixer import Mixer
from ui.campo_editavel import CampoEditavel


class MixBotao(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, mixer: Mixer, campos_texto: list[CampoEditavel]):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        self.button = ctk.CTkButton(self, width=50, height=50, corner_radius=10, 
                                    text="▶︎", font=("Helvetica", 40, "bold"), fg_color="transparent", 
                                    command=lambda:self.inicia_mixer(mixer=mixer, campos_texto=campos_texto))

        self.button.grid(row=0, column=0, sticky="ne", padx=20, pady=10)

    def inicia_mixer(self, mixer: Mixer, campos_texto: list[CampoEditavel]):
        mixer.start(campos_texto)

    def get_arquivo_usuario(self) -> str: 
        file = filedialog.asksaveasfilename(
            initialfile="untitled.wav",
            defaultextension=".wav",
            filetypes=[("wav", "*.wav"), ("mp3", "*.mp3"), ("ogg", "*.ogg")])
        return file



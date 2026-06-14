
import customtkinter as ctk

from mixer import Mixer

class Reproducao(ctk.CTkFrame):
    def __init__(self, master, mixer: Mixer):
        super().__init__(master)

        self.grid_columnconfigure((1,2), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.play_button = ctk.CTkButton(self, width=45, height=40, corner_radius=25, text="▶", command=lambda: mixer.on_play())
        self.play_button.grid(row=0, column=1, sticky="e")

        self.pause_button = ctk.CTkButton(self, width=45, height=40, corner_radius=25, text="||", command=lambda: mixer.on_pause())
        self.pause_button.grid(row=0, column=2, sticky="w", padx=5)

        


import customtkinter as ctk

from mixer import Mixer

class Reproducao(ctk.CTkFrame):
    def __init__(self, master, mixer: Mixer):
        super().__init__(master)

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.pause_button = ctk.CTkButton(self, width=50, height=40, corner_radius=30, text="||", command=lambda: mixer.on_pause())
        self.pause_button.grid(row=0, column=1, sticky="e")

        self.play_button = ctk.CTkButton(self, width=50, height=40, corner_radius=30, text="▶", command=lambda: mixer.on_play())
        self.play_button.grid(row=0, column=1, sticky="w", padx=75)
        
        self.volume = ctk.CTkSlider(self, width=170, height=10, corner_radius=30)
        self.volume.grid(row=0, column=2, sticky="e")


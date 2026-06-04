
import customtkinter as ctk

from mixer import Mixer

class Reproducao(ctk.CTkFrame):
    def __init__(self, master, mixer: Mixer):
        super().__init__(master)

        self.grid_columnconfigure((0, 1, 2), weight=1)
        
        self.pause_button = ctk.CTkButton(self, width=50, height=50, corner_radius=30, text="||", command=mixer.pause())
        self.pause_button.grid(row=0, column=1)



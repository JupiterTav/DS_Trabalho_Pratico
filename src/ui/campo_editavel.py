import customtkinter as ctk 

class CampoEditavel(ctk.CTkTextbox):
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.param_oitava = ctk.CTkEntry(self, width=30, height=15, corner_radius=-0, placeholder_text="oitava")
        self.param_oitava.grid(row=0, column=0, sticky="nw")

        self.param_volume = ctk.CTkEntry(self, width=30, height=15, corner_radius=0, placeholder_text="volume")
        self.param_volume.grid(row=0, column=0, sticky="nw", ipadx=5)

        self.param_instrumento = ctk.CTkEntry(self, width=30, height=15, corner_radius=0, placeholder_text="instrumento")
        self.param_instrumento.grid(row=0, column=1, sticky="ne")

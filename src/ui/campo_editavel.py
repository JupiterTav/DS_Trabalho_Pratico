import customtkinter as ctk 

class CampoEditavel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0,1), weight=1)

        self.campo_texto = ctk.CTkTextbox(self, width=500, height=50, corner_radius=0)
        self.campo_texto.grid(row=0, column=0, columnspan=2, sticky="ew")
        
        self.param_oitava = ctk.CTkEntry(self, width=70, height=15, corner_radius=-0, placeholder_text="oitava")
        self.param_oitava.grid(row=1, column=0, padx=1, sticky="nw")

        self.param_volume = ctk.CTkEntry(self, width=70, height=15, corner_radius=0, placeholder_text="volume")
        self.param_volume.grid(row=1, column=0, sticky="n")

        self.param_instrumento = ctk.CTkEntry(self, width=100, height=15, corner_radius=0, placeholder_text="instrumento")
        self.param_instrumento.grid(row=1, column=1, sticky="ne")

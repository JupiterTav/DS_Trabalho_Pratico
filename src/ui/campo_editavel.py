import customtkinter as ctk 

class CampoEditavel(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkScrollableFrame, oitava_inicial, volume_inicial, instrumento_inicial):

        super().__init__(master)
        
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0,1), weight=1)

        self.campo_texto = ctk.CTkEntry(self, width=750, height=70, corner_radius=10, font=("Arial", 16))
        self.campo_texto.grid(row=0, column=0, columnspan=2, sticky="ew")
        
        self.param_oitava = ctk.CTkEntry(self, width=30, height=15, corner_radius=5, placeholder_text=oitava_inicial)
        self.param_oitava.grid(row=1, column=0, padx=0, sticky="nw")

        self.param_volume = ctk.CTkEntry(self, width=70, height=15, corner_radius=5, placeholder_text=volume_inicial)
        self.param_volume.grid(row=1, column=0, sticky="n")

        self.param_instrumento = ctk.CTkEntry(self, width=70, height=15, corner_radius=5, placeholder_text=instrumento_inicial)
        self.param_instrumento.grid(row=1, column=1, sticky="ne")

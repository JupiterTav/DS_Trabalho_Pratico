import customtkinter as ctk

class Cabecalho(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure((0), weight=1)

        self.nome_arquivo = ctk.CTkEntry(self, placeholder_text="título")
        self.nome_arquivo.grid(row=0, column=0, sticky="ew", padx=(0, 30))
        
        self.download_button = ctk.CTkButton(self, width=30, height=30 ,text="↓", corner_radius=50)
        self.download_button.grid(row=0, column=1, padx=(10, 0), sticky="e")

        self.download_button.grid_anchor("ne")

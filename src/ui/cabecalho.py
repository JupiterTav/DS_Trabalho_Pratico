import customtkinter as ctk

class Cabecalho(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure((0), weight=1)

        self.upload_txt = ctk.CTkButton(self, width=30, height=30, text="↑", corner_radius=50)
        self.upload_txt.grid(row=0, column=0, sticky="w", padx=(0, 10))
        
        self.download_button = ctk.CTkButton(self, width=30, height=30 ,text="↓", corner_radius=50)
        self.download_button.grid(row=0, column=1, padx=(10, 0), sticky="e")

        self.download_button.grid_anchor("ne")

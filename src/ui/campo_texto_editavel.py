import customtkinter as ctk


class CampoTextoEditavel(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkScrollableFrame, oitava_inicial, volume_inicial, instrumento_inicial):
        super().__init__(master)

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.campo_texto = ctk.CTkEntry(self, width=850, height=50, corner_radius=5, font=("Arial", 16))
        self.campo_texto.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.text_oitava = ctk.CTkLabel(self, text="Oitava inicial:", font=("Arial", 14, "bold"))
        self.param_oitava = ctk.CTkEntry(self, width=30, height=15, corner_radius=2)
        self.param_oitava.insert(0, oitava_inicial)
        self.text_oitava.grid(row=1, column=0, sticky="w", pady=5)
        self.param_oitava.grid(row=1, column=0, sticky="w", padx=(100, 0), pady=2)

        self.text_volume = ctk.CTkLabel(self, text="Volume inicial: ", font=("Arial", 14, "bold"))
        self.param_volume = ctk.CTkEntry(self, width=70, height=15, corner_radius=2)
        self.param_volume.insert(0, volume_inicial)
        self.text_volume.grid(row=1, column=0, sticky="e", padx=(0, 260), pady=2)
        self.param_volume.grid(row=1, column=0, sticky="e", padx=(0, 190), pady=2)

        self.text_instrumento = ctk.CTkLabel(self, text="Instrumento GM: ", font=("Arial", 14, "bold"))
        self.param_instrumento = ctk.CTkEntry(self, width=60, height=15, corner_radius=2,
                                              placeholder_text=instrumento_inicial)
        self.param_instrumento.insert(0, instrumento_inicial)
        self.text_instrumento.grid(row=1, column=1, sticky="e", padx=(0, 75), pady=2)
        self.param_instrumento.grid(row=1, column=1, sticky="e")

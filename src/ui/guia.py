import customtkinter as ctk

ctk.set_appearance_mode("light")


class Guia(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        self.title("Guia de documentação")
        self.geometry("600x800")

        main_frame = ctk.CTkFrame(self, corner_radius=20)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        header = ctk.CTkFrame(main_frame)
        header.pack(fill="x")

        header.grid_columnconfigure(0, weight=1)
        header.grid_columnconfigure(1, weight=3)

        ctk.CTkLabel(
            header,
            text="Símbolo",
            font=("Arial", 14, "bold")
        ).grid(row=0, column=0, sticky="ew", pady=5)

        ctk.CTkLabel(
            header,
            text="Informação",
            font=("Arial", 14, "bold")
        ).grid(row=0, column=1, sticky="ew", pady=5)

        self.scroll = ctk.CTkScrollableFrame(main_frame, border_width=2)
        self.scroll.pack(fill="both", expand=True)

        self.scroll.grid_columnconfigure(0, weight=1)
        self.scroll.grid_columnconfigure(1, weight=3)

        dados = [
            ("[N]", "atrasa a melodia da voz em questão em N beats. N >= 0"),
            ("Instrumentos", "Instrumentos são representados em General MIDI e vão de 0 até 127"),
            ("▶︎", "Aperte para gerar a música e os arquivos"),
            ("Saída", "Gera um arquivo de som e um arquivo MIDI na pasta escolhida"),
            ("BPM",
             "O BPM (batidas por minuto) é uma medida global, alterá-lo (com < ou >)\n em uma voz alterará em todas"),
            ("A", "Nota Lá"),
            ("B", "Nota Si"),
            ("C", "Nota Dó"),
            ("D", "Nota Ré"),
            ("E", "Nota Mi"),
            ("F", "Nota Fá"),
            ("G", "Nota Sol"),
            ("H", "Nota Si Bemol"),
            ("Eb/Mb", "Nota Mi Bemol"),
            ("Ab", "Nota Lá Bemol"),
            ("a/b/c/d/e/f/g/h", "Pausa"),
            ("< e >", "decrementa e incrementa o bpm em 10, respectivamente."),
            ("Espaço", "Aumenta volume para o dobro (máximo 127)"),
            ("!", "Instrumento General MIDI #24 (Bandoneon)"),
            ("O/o/U/u/I/i", "Instrumento General MIDI #110 (Gaita de Foles)"),
            ("Consoante", "Caso o simbolo anterior seja uma Nota, repete, senão pausa"),
            ("Dígito par", "Instrumento = instrumento atual + valor do dígito"),
            ("?.", "Incrementa uma oitava (máx. 9)"),
            ("V", "Decresce uma oitava (min. 0"),
            ("; ou dígito ímpar", "Instrumento General MIDI #15 (Tubular Bells)"),
            (",", "Instrumento General MIDI #114 (Agogô)"),
            ("Outros simbolos", "Caso o simbolo anterior seja uma Nota, repete, senão pausa"),
        ]

        for row, (simbolo, descricao) in enumerate(dados):
            self.criar_linha(row, simbolo, descricao)

    def criar_linha(self, row, simbolo, descricao):
        ctk.CTkLabel(
            self.scroll,
            text=simbolo,
            anchor="w",
        ).grid(row=row, column=0, sticky="ew", padx=10, pady=5)

        ctk.CTkLabel(
            self.scroll,
            text=descricao,
            anchor="w"
        ).grid(row=row, column=1, sticky="ew", padx=10, pady=5)

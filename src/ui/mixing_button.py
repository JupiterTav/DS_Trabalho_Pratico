from tkinter import filedialog

import customtkinter as ctk


class MixBotao(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, action_callback, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.button = ctk.CTkButton(self, width=50, height=20, corner_radius=10,
                                    text="▶︎", font=("Helvetica", 40, "bold"), fg_color="transparent",
                                    command=lambda: self.inicia_mixer(action_callback))

        self.button.grid(row=0, column=0, sticky="ne", padx=20, pady=10)

    def inicia_mixer(self, action_callback):
        # Desabilita o botão para evitar múltiplos cliques e indica processamento
        self.button.configure(state="disabled", text="⏳")

        def on_finish_callback():
            # Devolve o botão ao estado normal após o sucesso
            self.after(0, lambda: self.button.configure(state="normal", text="▶︎"))

        def on_error_callback(mensagem):
            # Devolve o botão ao estado normal após erro
            self.after(0, lambda: self.button.configure(state="normal", text="▶︎"))
            print(f"[ERRO NA UI] Algo falhou na geração: {mensagem}")

        # Delega a execução para o coordenador (JanelaPrincipal)
        action_callback(on_finish_callback, on_error_callback)

    def get_arquivo_usuario(self) -> str:
        file = filedialog.asksaveasfilename(
            initialfile="untitled.wav",
            defaultextension=".wav",
            filetypes=[("wav", "*.wav"), ("mp3", "*.mp3"), ("ogg", "*.ogg")])
        return file

import customtkinter as ctk
from tkinter import filedialog


class BakeBotao(ctk.CTkFrame):
    def __init__(self, master: ctk.CTk, mixer):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        self.button = ctk.CTkButton(self, width=50, height=50, corner_radius=10, text="▶︎", font=("Helvetica", 40, "bold"), fg_color="transparent")
        self.button.grid(row=0, column=0, sticky="ne", padx=20, pady=10)


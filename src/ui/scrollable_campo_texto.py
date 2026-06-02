import customtkinter as ctk
from .campo_editavel import CampoEditavel


class ScrollableCampoTexto(ctk.CTkScrollableFrame):
    def __init__(self, master, value):
        super().__init__(master)
        
        self.grid_columnconfigure(0, weight=1)
        self.value = value

        self.campos = []

        for i in range(0, self.value):
            camp_edit = CampoEditavel(self)
            camp_edit.grid(row=i, column=0, ipady=15)

        

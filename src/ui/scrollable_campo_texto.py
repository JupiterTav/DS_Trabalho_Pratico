import customtkinter as ctk
from .campo_editavel import CampoEditavel


class ScrollableCampoTexto(ctk.CTkScrollableFrame):
    def __init__(self, master, value):
        super().__init__(master)
        
        self.grid_columnconfigure(0, weight=1)
        self.value = 0 

        self.campos = []

        self.adiciona_campo()


    def adiciona_campo(self) -> CampoEditavel: 
        self.value += 1

        camp_edit = CampoEditavel(self) 
        camp_edit.grid(row=self.value, column=0, ipady=15)
        
        self.campos.append(camp_edit)
        
        print(f"[SCROLLABLE CAMPO TEXTO] {self.value} | campos: {len(self.campos)}")
        self.__desenha_add_button()
        return camp_edit

    def __desenha_add_button(self): 
        add_button = ctk.CTkButton(self, width=30, height=30, corner_radius=20, text="+", font=("Arial", 18), command=lambda: self.adiciona_campo())
        add_button.grid(row=self.value+1, column=0)

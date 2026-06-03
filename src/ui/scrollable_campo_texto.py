import customtkinter as ctk
from .campo_editavel import CampoEditavel


class ScrollableCampoTexto(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.grid_columnconfigure(0, weight=1)
        self._quant_campos = 1 

        
        self.__ciclo_valores_iniciais: int = 0
        self.__oitavas_padrao = ["6", "5", "4", "3"]
        self.__volumes_padrao = ["100", "80", "60", "40"]
        self.__instrumentos_padrao = ["6", "20", "0", "70"]

        self.campos: list[CampoEditavel] = []
        self.campos.append(self.adiciona_campo())


    def adiciona_campo(self) -> CampoEditavel: 
        if self.__ciclo_valores_iniciais % 4 == 0:
            self.__ciclo_valores_iniciais = 0 
            
        camp_edit: CampoEditavel = CampoEditavel(self, 
                                  oitava_inicial=self.__oitavas_padrao[self.__ciclo_valores_iniciais], 
                                  volume_inicial=self.__volumes_padrao[self.__ciclo_valores_iniciais], 
                                  instrumento_inicial=self.__instrumentos_padrao[self.__ciclo_valores_iniciais]) 
        camp_edit.grid(row=self._quant_campos, column=0, ipady=15)
        
        self.__ciclo_valores_iniciais += 1
        
        print(f"[SCROLLABLE CAMPO TEXTO] {self._quant_campos}")
        self._quant_campos += 1
        
    
        self.__desenha_add_button()
        
        return camp_edit

    def __desenha_add_button(self): 
        add_button = ctk.CTkButton(self, width=30, height=30, corner_radius=20, text="+", font=("Arial", 18), command=lambda: self.adiciona_campo())
        add_button.grid(row=self._quant_campos , column=0)

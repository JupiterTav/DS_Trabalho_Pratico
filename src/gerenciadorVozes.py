from leitorTexto import LeitorTexto
from voz import Voz


class GerenciadorVozes:
    def __init__(self):
        self.vozes = []

    def criar_vozes(self, texto: LeitorTexto()):
        i = len(texto.linhas)
        for linha in texto.linhas:
            voz = Voz(linha, 170, 20*i,  i)
            self.vozes.append(voz)

    def get_vozes(self):
        return self.vozes

    def len_vozes(self):
        return len(self.vozes)

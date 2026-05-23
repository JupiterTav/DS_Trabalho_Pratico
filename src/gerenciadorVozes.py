from leitorTexto import LeitorTexto
from voz import Voz


class GerenciadorVozes:
    vozes = []

    def criar_vozes(self, texto: LeitorTexto()):
        i = len(texto)
        for linha in texto.linhas:
            voz = Voz(linha, 170, 20*i,  i)
            self.vozes.append(voz)

    def get_vozes(self):
        print(len(self.vozes))
        for voz in self.vozes:
            print(voz.voz_texto)



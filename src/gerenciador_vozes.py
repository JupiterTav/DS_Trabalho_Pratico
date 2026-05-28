from track import Track as Voz
from campo_texto import CampoTexto


class GerenciadorVozes:
    def __init__(self):
        self.__vozes = list(Voz)
        self.bpm_global = 120

        self.__oitavas_padrao = [6, 5, 4, 3]
        self.__volumes_padrao = [100, 80, 60, 40]

    def gerar(self, texto: CampoTexto()):
        i = 0
        for linha in texto.linhas:
            if i % 4 == 0:
                i = 0
            voz = Voz(linha, self.__volumes_padrao[i], self.__oitavas_padrao[i])
            self.__vozes.append(voz)
            i += 1

    @property
    def vozes(self):
        return self.__vozes

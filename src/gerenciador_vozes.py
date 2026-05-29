from track import Track as Voz
from campo_texto import CampoTexto


class GerenciadorVozes:
    def __init__(self):
        self.bpm_global = 120

        self.__oitavas_padrao = [6, 5, 4, 3]
        self.__volumes_padrao = [100, 80, 60, 40]

    def gerar_vozes(self, texto: CampoTexto()) -> list[Voz]:
        vozes = []
        i = 0
        for linha in texto.linhas:
            if i % 4 == 0:
                i = 0
            voz = Voz(linha, self.__volumes_padrao[i], self.__oitavas_padrao[i])
            vozes.append(voz)
            i += 1
        return vozes


from .track import Track as Voz


class GeradorVozes:
    def __init__(self):
        self.bpm_global: int = 120

        self.__oitavas_padrao = [6, 5, 4, 3]
        self.__volumes_padrao = [100, 80, 60, 40]

    def gerar_vozes(self, texto: list[str]) -> list[Voz]:
        vozes: list[Voz] = []
        i = 0

        for linha in texto:
            voz = None
            if i % 4 == 0:
                i = 0
            if '[' and ']' in linha and linha[0] == '[':
                close_bracket_index = linha.index(']')
                linha_correta = linha[close_bracket_index+1:] 
                voz = Voz(linha_correta, self.__volumes_padrao[i], self.__oitavas_padrao[i])
                voz.delay = (int(linha[1:close_bracket_index]))
            else:
                voz = Voz(linha, self.__volumes_padrao[i], self.__oitavas_padrao[i])

            vozes.append(voz)
            i += 1

        return vozes


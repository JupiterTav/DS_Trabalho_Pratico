from leitorTexto import LeitorTexto
from voz import Voz


class GerenciadorVozes:
    def __init__(self):
        self.vozes = []
        self.bpm_global = 120

    def criar_vozes(self, texto: LeitorTexto()):
        i = 0
        oitavas_base = [6, 5, 4, 3]
        volumes_base = [100, 80, 60, 40]

        for linha in texto.linhas:
            if i % 4 == 0:
                i = 0
            print(f"linha {i}")

            voz = Voz(linha, self.bpm_global, volumes_base[i], oitavas_base[i])
            self.vozes.append(voz)
            i += 1
    def get_vozes(self):
        return self.vozes

    def len_vozes(self):
        return len(self.vozes)

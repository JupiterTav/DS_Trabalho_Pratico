from parametros import Parametros


class Voz:
    def __init__(self, texto, bpm, volume, oitava):
        self.voz_texto = texto
        self.parametros = Parametros(bpm, volume, oitava)

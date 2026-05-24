from parametros import Parametros


class Voz:
    def __init__(self, texto, bpm, volume, oitava):
        self.voz_texto = texto
        self.parametros = Parametros(bpm, volume, oitava)
        self.bpm = bpm
        self.volume = volume
        self.oitava = oitava

        self.nota = 00
        self.instrumento = 00

    def get_bpm(self):
        return self.bpm

    def set_bpm(self, novoBpm):
        self.bpm = novoBpm
        return self.bpm

    def get_volume(self):
        return self.volume

    def set_volume(self, novoVolume):
        self.volume = novoVolume

    def get_oitava(self):
        return self.oitava

    def set_oitava(self, novaOitava):
        self.oitava = novaOitava

    def set_nota(self, nota):
        self.nota = nota

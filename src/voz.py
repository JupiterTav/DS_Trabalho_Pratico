class Voz:
    def __init__(self, texto, bpm, volume, oitava):
        self.voz_texto = texto
        self.__bpm = bpm
        self.__volume = volume
        self.__oitava = oitava
        self.__oitavadefault = oitava
        self.__atraso = 00
        self.nota = 00
        self.instrumento = 00

    def get_bpm(self):
        return self.__bpm

    def set_bpm(self, novoBpm):
        self.bpm = novoBpm

    def get_volume(self):
        return self.__volume

    def set_volume(self, novoVolume):
        self.volume = novoVolume

    def dobra_volume(self):
        if(self.volume*2 > 127):
            self.volume = 127
        else: 
            self.volume = self.volume*2

    def get_oitava(self):
        return self.__oitava

    def set_oitava(self, novaOitava):
        if novaOitava <= 9 and novaOitava >= 0:
            self.oitava = novaOitava
        else:
            self.oitava = self.__oitavadefault

    def set_nota(self, nota):
        self.nota = nota

    def set_atraso(self, atraso):
        self.__atraso = atraso

    def get_atraso(self):
        atraso = self.__atraso
        self.__atraso = 0
        return atraso

    def get_instrumento(self):
        return self.instrumento

    def set_instrumento(self, gm_midi_instrument):
        if gm_midi_instrument > 127:
            self.instrumento = 0
        else:
            self.instrumento = gm_midi_instrument

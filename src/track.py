class Track:
    __VOLUME_MAXIMO = 127

    def __init__(self, texto_track: str, volume: int, oitava: int):
        self.__texto_track = texto_track
        self.__volume = volume
        self.__oitava = oitava

        self.__oitava_padrao = oitava
        self.__instrumento = 0
        self.__delay = 0
        self.__nota = 0

        self.nota_atual: int = 0

    @property
    def texto_track(self):
        return self.__texto_track

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value: int):
        if value > self.__VOLUME_MAXIMO:
            self.__volume = self.__VOLUME_MAXIMO
        elif value < 0:
            self.__volume = 0
        else:
            self.__volume = value

    @property
    def oitava(self):
        return self.__oitava

    @oitava.setter
    def oitava(self, value: int):
        if value <= 9 and value >= 0:
            self.__oitava = value
        else:
            self.__oitava = self.__oitava_padrao

    @property
    def delay(self):
        if self.__delay > 0:
            delayed = self.__delay
            self.__delay = 0
            return delayed
        else:
            return self.__delay

    @delay.setter
    def delay(self, value: int):
        if value >= 0:
            self.__delay = value
        else:
            raise Exception("delay não deve ser negativo")

    def eh_atrasado(self) -> bool:
        if '[' and ']' in self.texto_track and self.texto_track[0] == '[':
            return True 
        return False 

    @property
    def instrumento(self):
        return self.__instrumento

    @instrumento.setter
    def instrumento(self, value: int ):
        if value >= 1 and value <= 128:
            self.__instrumento = value
        else:
            raise Exception(f"não há intrumento general midi {value}")
    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, value: int):
        self.__nota = value
        self.nota_atual = value + (12 * self.oitava)

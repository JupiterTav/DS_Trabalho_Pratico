# TODO: configurar os parametros de uma track
# TODO: Construir metodos relacionados a track (mido)


class Track:
    __VOLUME_MAXIMO = 127

    def __init__(self, texto_track: str, volume: int, oitava: int):
        self.__texto_track = texto_track
        self.__volume = volume
        self.__oitava = oitava

        self.__oitava_padrao = oitava
        self.__nota_atual = 0
        self.__instrumento_atual = 0
        self.__delay = 0

    @property
    def texto_track(self):
        return self.__texto_track

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
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
    def oitava(self, value):
        if value <= 9 and value >= 0:
            self.__oitava = value
        else:
            self.__oitava = self.__oitava_padrao

    @property
    def delay(self):
        return self.__delay

    @delay.setter
    def delay(self, value):
        if value >= 0:
            self.__delay = value
        else:
            raise Exception("delay não deve ser negativo")



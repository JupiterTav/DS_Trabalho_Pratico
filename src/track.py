# TODO: configurar os parametros de uma track [X]
# WARN: Mover esses métodos relacionados para  uma classe de eventos midi
    # TODO: Construir metodos relacionados a track (mido)

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

        self.nota_atual = 0
#  NOTE: Interessante encapsular numa classe parametros(track.parametro.nome_parametro)

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

    @delay.setter
    def delay(self, value):
        if value >= 0:
            self.__delay = value
        else:
            raise Exception("delay não deve ser negativo")

    def eh_delayed(self) -> bool:
         if '[' and ']' in self.texto_track and self.texto_track[0] == '[':
                return True 

           @property
    def instrumento(self):
        return self.__instrumento

    @instrumento.setter
    def instrumento(self, value):
        if value >= 1 and value <= 128:
            self.__instrumento = value
        else:
            raise Exception(f"não há intrumento general midi {value}")
    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, value):
        self.__nota = value
        self.nota_atual = value + (12 * self.oitava)


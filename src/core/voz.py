from typing import override

from core import config_mapeamento
from core.characteres.Icharacter import ICharacter
from core.characteres.character_global import CharacterGlobal
from core.characteres.character_instrumento import CharacterInstrumento
from core.characteres.character_nota import CharacterNota
from core.characteres.character_pausa import CharacterPausa
from core.characteres.character_voz import CharacterVoz
from core.interpretador import Interpretador


class Voz(Interpretador):
    """Classe Voz
        Interpretador que representa seu texto e parametros tocados numa nota
    """
    __VOLUME_MAXIMO = 127

    def __init__(self, texto_track: str, volume: int, oitava: int, channel: int):
        super().__init__()
        self.__texto_track = texto_track

        self.__volume = volume
        self.__oitava = oitava

        self.__instrumento = 0
        self.__oitava_padrao = oitava

        self.channel = channel

        self.__delay = self.calcula_delay(texto_track)
        self.__nota = 0
        self.__nota_repetivel = ""

        for i, char in enumerate(texto_track):
            if i + 1 < len(texto_track) and char in 'M' and texto_track[i + 1] == 'b':
                char = 'Mb'

    ## @param char Character a ser interpretado
    @override
    def interpretar(self, char: str) -> ICharacter:
        """Interpretar Doc: Retorna o tipo de caractere correto para cada mapeamento"""
        super().interpretar(char)

        if char in config_mapeamento.notas_midi:
            self.nota = config_mapeamento.notas_midi[char]
            self.__nota_repetivel = self.nota
            return CharacterNota(self.nota, self)

        elif char in config_mapeamento.character_pausa:
            self.__nota_repetivel = -1
            return CharacterPausa(char, self)

        elif char in config_mapeamento.character_global:
            self.__nota_repetivel = -1
            return CharacterGlobal(char, self)
        elif char in config_mapeamento.gm_intruments or char.isnumeric():
            self.__nota_repetivel = -1
            return CharacterInstrumento(char, self)

        elif char in config_mapeamento.character_voz:
            self.__nota_repetivel = -1
            return CharacterVoz(char, self)
        else:
            if self.__nota_repetivel != -1:
                return CharacterNota(self.__nota_repetivel, self)
            else:
                return CharacterPausa(self.nota, self)

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
        if value >= 0 and value <= 9:
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

    def calcula_delay(self, texto_track: str) -> int:
        if '[' and ']' in texto_track and texto_track[0] == '[':
            inicio = texto_track.index(']') + 1
            self.__texto_track = texto_track[inicio:]
            return int(texto_track[1:texto_track.index(']')])
        return 0

    @property
    def instrumento(self):
        return self.__instrumento

    @instrumento.setter
    def instrumento(self, value: int):
        if value >= 0 and value <= 127:
            self.__instrumento = value
        else:
            raise Exception(f"não há intrumento general midi {value}")

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, value: int):
        self.__nota = value + (12 * self.__oitava)

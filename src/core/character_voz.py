from core import config_mapeamento
from core.Icharacter import ICharacter
from core.voz import Voz

class CharacterVoz(ICharacter):
    def __init__(self, char, voz: Voz):
        super().__init__(char)
        self.voz = voz

    def character_comando(self):
        if self.nota in config_mapeamento.gm_intruments:
            self.voz.instrumento = config_mapeamento.gm_intruments[self.nota]
        elif self.nota.isnumeric():
            valor = int(self.nota)
            self.voz.instrumento = self.voz.instrumento + valor if valor % 2 == 0 else 14

        elif self.nota in '?.':
            self.voz.oitava += 1
        elif self.nota == 'V':
            self.voz.oitava -= 1
        elif self.nota == ' ':
            self.voz.volume *= 2

    def character_comando_midi(self):
        pass
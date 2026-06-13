from core import config_mapeamento
from core import Icharacter, character_nota, character_pausa, character_instrumento
from core.character_global import CharacterGlobal


class Interpretador:
    def __init__(self):
        self.characteres: list[Icharacter.ICharacter] = []
        pass
    def interpretar(self, char: str) -> None:
        return None
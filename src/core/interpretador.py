from core import config_mapeamento
from core import Icharacter, character_nota, character_pausa, character_instrumento
from core.character_global import CharacterGlobal


class Interpretador:
    def __init__(self):
        self.characteres: list[Icharacter.ICharacter] = []
        pass
    def interpretar(self, char: str) -> None:
        if char in config_mapeamento.notas_midi:
            self.characteres.append(character_nota.CharacterNota(config_mapeamento.notas_midi[char]))
        elif char in config_mapeamento.character_pausa:
            self.characteres.append(character_pausa.CharacterPausa(char))
        elif char in config_mapeamento.character_global:
            self.characteres.append(CharacterGlobal(char))
        return None
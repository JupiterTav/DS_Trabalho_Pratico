from core import config_mapeamento, Icharacter, character_nota


class Interpretador:
    def __init__(self):
        self.characteres: list[Icharacter.ICharacter] = []
        pass
    def interpretar(self, char: str):
        if char in config_mapeamento.notas_midi:
            self.characteres.append(character_nota.CharacterNota(config_mapeamento.notas_midi[char]))

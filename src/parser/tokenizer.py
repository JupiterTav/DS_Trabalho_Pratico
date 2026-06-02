import re
import logging
from src.parser.ast_nodes import MusicNode

class RegexTokenizer:
    def __init__(self):
        # A-G with optional b/# and optional octave digit, [n] for pauses, <n> for tempo
        self.pattern = re.compile(r'([A-G][b#]?\d?)|(\[\d+\])|(<\d+>)|(\S)', re.IGNORECASE)
    
    def parse(self, text: str) -> list[MusicNode]:
        nodes = []
        current_bpm = 120
        current_duration_ms = 60000.0 / current_bpm

        for match in self.pattern.finditer(text):
            note, duration, tempo, garbage = match.groups()
            
            if note:
                nodes.append(MusicNode(tipo='NOTA', valor=note.upper(), duration_ms=current_duration_ms))
            elif duration:
                val = duration.strip('[]')
                nodes.append(MusicNode(tipo='PAUSA', valor=val, duration_ms=0))
            elif tempo:
                try:
                    bpm = int(tempo.strip('<>'))
                    current_bpm = bpm
                    current_duration_ms = 60000.0 / current_bpm
                    nodes.append(MusicNode(tipo='TEMPO', valor=str(bpm), duration_ms=0))
                except ValueError:
                    pass
            elif garbage:
                logging.warning(f"Ignored syntax garbage: {garbage}")
        
        return nodes

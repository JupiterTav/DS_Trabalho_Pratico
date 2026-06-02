from dataclasses import dataclass

@dataclass(slots=True)
class MusicNode:
    tipo: str
    valor: str
    duration_ms: float = 500.0

from core.track import Track


class Voz(Track):
    def __init__(self, texto_track: str, volume: int, oitava: int):
        super().__init__(texto_track, volume, oitava)


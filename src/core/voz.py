from core.track import Track


class Voz(Track):
    def __init__(self, texto_track: str, volume: int, oitava: int):
        super().__init__(texto_track, volume, oitava)
        self.delay: int = self.calcula_delay(texto_track)

    def calcula_delay(self, texto_track: str) -> int:
        if '[' and ']' in texto_track and texto_track[0] == '[':
            return (int(texto_track[1:texto_track.index(']')]))

        return 0

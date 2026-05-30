from track import Track


class EventosTrack():
    def __init__(self):
        self.track_event = ['?', '.', 'V']

    def is_track_evento(self, *, char: str):
        if char in self.track_event:
            return True
        return False

    def interpreta_track_evento(self, *, char: str, voz: Track):
        if char == '?' or '.':
            voz.oitava += 1
        elif char == self.track_event[2]:
            voz.oitava -= 1

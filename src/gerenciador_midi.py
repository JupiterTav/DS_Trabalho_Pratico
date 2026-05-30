import os
from mido import Message, MetaMessage, MidiTrack, MidiFile
from track import Track
from eventos_midi import EventosMidi
from gerador_vozes import GeradorVozes


class GerenciadorMidi():

    def __init__(self):
        super().__init__()

        self.evento_midi = EventosMidi()
        self.__arq_midi = MidiFile(type=1, ticks_per_beat=480)
        self.__caminho = ""

    def gerarArquivo(self, caminho: str):
        try:
            os.makedirs(os.path.dirname(caminho), exist_ok=True)

            if ".midi" or ".mid" not in caminho:
                self.__caminho = caminho + ".mid"
            else:
                self.__caminho = caminho

            self.__arq_midi.save(self.__caminho)

        except OSError as e:
            print(f"Ocorreu um erro no sistema, {e}")
        except PermissionError:
            print("Permissão negada para criação do arquivo")

        return 0

    def processaTracks(self, vozes: Track, global_vozes: GeradorVozes):
        for i, voz in enumerate(vozes):
            track = self.criaTrack(track_name=f'voz {i}')
            track.append(MetaMessage('text', text=f'Melodia da voz {i}', time=0))
            track.append(self.evento_midi.define_volume(channel=i, volume=voz.volume))
            track.append(self.evento_midi.define_tempo(bpm=global_vozes.bpm_global))

            for j, char in enumerate(voz.texto_track):
                if char in (self.evento_midi._notas_midi or self.evento_midi._gm_intruments or 'abcdefgh' or char.isnumeric()):
                    self.evento_midi.interpretaEventoMidi(voz.texto_track[j], channel=i, voz=voz, track=track)

                elif char in '?.':
                    voz.oitava += 1
                elif char in 'V':
                    voz.oitava -= 1
                elif char in '>':
                    global_vozes.bpm_global += 10
                    track.append(self.evento_midi.define_tempo(bpm=global_vozes.bpm_global))
                elif char in '<':
                    global_vozes.bpm_global -= 10
                    track.append(self.evento_midi.define_tempo(bpm=global_vozes.bpm_global))

                else:
                    if voz.texto_track[j-1] in self.evento_midi._notas_midi:
                        self.evento_midi.interpretaEventoMidi(voz.texto_track[j-1], channel=i, voz=voz, track=track)
                    else:
                        self.evento_midi.interpretaEventoMidi(voz.texto_track[j], channel=i, voz=voz, track=track)

    def criaTrack(self, *, track_name: str):
        track = MidiTrack()
        self.__arq_midi.tracks.append(track)
        track.name = track_name

        self.__arq_midi.save(self.__caminho)

        return track

    def salvaArquivo(self):
        self.__arq_midi.save(self.__caminho)

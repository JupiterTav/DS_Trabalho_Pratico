import mido
from src.parser.ast_nodes import MusicNode

class MidiBuilder:
    @staticmethod
    def build_midi(nodes: list[MusicNode], export_path: str):
        mid = mido.MidiFile()
        track = mido.MidiTrack()
        mid.tracks.append(track)

        # Base note values
        base_notes = {'C': 60, 'C#': 61, 'D': 62, 'D#': 63, 'E': 64, 'F': 65,
                      'F#': 66, 'G': 67, 'G#': 68, 'A': 69, 'A#': 70, 'B': 71}
        
        current_pause_ticks = 0
        
        for node in nodes:
            if node.tipo == 'NOTA' or node.tipo == 'nota':
                # Parse note to midi pitch
                val = node.valor.upper()
                base = val[0]
                pitch = base_notes.get(base, 60)
                
                # Check for sharps/flats and octaves
                idx = 1
                if len(val) > 1 and val[1] in ('#', 'b'):
                    if val[1] == '#': pitch += 1
                    elif val[1] == 'B': pitch -= 1
                    idx = 2
                    
                if len(val) > idx and val[idx].isdigit():
                    octave = int(val[idx])
                    pitch = pitch + (octave - 4) * 12

                track.append(mido.Message('note_on', note=pitch, velocity=64, time=current_pause_ticks))
                current_pause_ticks = 0 # reset after applying
                
                ticks = int((node.duration_ms / 1000.0) * mid.ticks_per_beat * 2) 
                track.append(mido.Message('note_off', note=pitch, velocity=64, time=ticks))
            elif node.tipo == 'PAUSA' or node.tipo == 'pausa':
                try:
                    pause_val = float(node.valor)
                    # Pause in beats -> convert to ticks
                    pause_ticks = int(pause_val * mid.ticks_per_beat)
                    current_pause_ticks += pause_ticks
                except: pass

        mid.save(export_path)

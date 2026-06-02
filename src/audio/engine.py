import pygame.midi
import pygame
import queue
import array
import math
from src.core.events import PlayNoteEvent, StopNoteEvent, SetVolumeEvent, SetInstrumentEvent, PlaySequenceEvent, StopSequenceEvent

class SynthFallback:
    def __init__(self):
        pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)
        self.active_channels = {}
        self.instrument_type = "sine"
        
    def set_instrument(self, inst_id):
        if inst_id < 40:
            self.instrument_type = "sine"
        elif inst_id < 80:
            self.instrument_type = "square"
        else:
            self.instrument_type = "sawtooth"
            
    def note_on(self, pitch, velocity=127):
        freq = 440.0 * (2.0 ** ((pitch - 69) / 12.0))
        sample_rate = 44100
        n_samples = int(sample_rate * 2.0)
        buf = array.array('h')
        
        max_amp = int(32767 * (velocity / 127.0))
        for i in range(n_samples):
            t = float(i) / sample_rate
            env = math.exp(-3.0 * t)
            
            if self.instrument_type == "sine":
                val = math.sin(2 * math.pi * freq * t)
            elif self.instrument_type == "square":
                val = 1.0 if math.sin(2 * math.pi * freq * t) > 0 else -1.0
            else:
                val = 2.0 * (freq * t - math.floor(freq * t + 0.5))
                
            buf.append(int(max_amp * val * env))
            
        sound = pygame.mixer.Sound(buffer=buf)
        channel = pygame.mixer.find_channel()
        if channel:
            channel.play(sound)
            self.active_channels[pitch] = channel
            
    def note_off(self, pitch, velocity=0):
        if pitch in self.active_channels:
            self.active_channels[pitch].fadeout(100)
            del self.active_channels[pitch]

class AudioEngine:
    def __init__(self, audio_queue: queue.Queue, gui_queue: queue.Queue):
        self.audio_queue = audio_queue
        self.gui_queue = gui_queue
        self.volume = 100
        self.player = None
        
        try:
            pygame.midi.init()
            for i in range(pygame.midi.get_count()):
                info = pygame.midi.get_device_info(i)
                if info[3] == 1: # Output device
                    try:
                        self.player = pygame.midi.Output(i, 0)
                        self.player.set_instrument(0)
                        print(f"MIDI Output Open: {info[1]}")
                        break
                    except Exception as e:
                        print(f"Skipping port {i}: {e}")
                        self.player = None
        except Exception as e:
            print("Failed to init pygame midi:", e)
            
        if not self.player:
            print("WARNING: Using Synthetic Fallback because MIDI failed!")
            self.player = SynthFallback()
            
        self.running = False
        
        # Base pitch dictionary
        self.pitch_map = {
            'C': 60, 'C#': 61, 'D': 62, 'D#': 63, 'E': 64, 'F': 65,
            'F#': 66, 'G': 67, 'G#': 68, 'A': 69, 'A#': 70, 'B': 71
        }

    def _get_pitch(self, note_str: str) -> int:
        val = note_str.upper()
        if not val:
            return 60
            
        base = val[0]
        pitch = self.pitch_map.get(base, 60)
        
        idx = 1
        if len(val) > 1 and val[1] in ('#', 'B'):
            if val[1] == '#': pitch += 1
            elif val[1] == 'B': pitch -= 1
            idx = 2
            
        if len(val) > idx and val[idx].isdigit():
            # For multi-digit octaves if ever needed
            import re
            m = re.search(r'\d+', val[idx:])
            if m:
                octave = int(m.group())
                pitch = pitch + (octave - 4) * 12
                
        return pitch

    def run(self):
        self.running = True
        while self.running:
            try:
                event = self.audio_queue.get(timeout=0.05)
                if isinstance(event, PlayNoteEvent):
                    pitch = self._get_pitch(event.nota)
                    print(f"[AudioEngine] PlayNote: {event.nota} -> {pitch} (Vol: {self.volume})")
                    if self.player:
                        self.player.note_on(pitch, self.volume)
                elif isinstance(event, StopNoteEvent):
                    pitch = self._get_pitch(event.nota)
                    if self.player:
                        self.player.note_off(pitch, self.volume)
                elif isinstance(event, SetVolumeEvent):
                    self.volume = event.volume
                    print(f"[AudioEngine] Volume: {self.volume}")
                elif isinstance(event, SetInstrumentEvent):
                    if self.player:
                        self.player.set_instrument(event.instrument_id)
                        print(f"[AudioEngine] Instrument: {event.instrument_id}")
                elif isinstance(event, PlaySequenceEvent):
                    if self.player:
                        self._play_sequence(event)
            except queue.Empty:
                pass
            except Exception as e:
                print("Error in AudioEngine:", e)

    def _play_sequence(self, event: PlaySequenceEvent):
        from time import sleep
        current_bpm = getattr(event, 'bpm', 120)
        beat_duration = 60.0 / current_bpm
        
        for node in event.nodes:
            if not self.running:
                break
                
            if not self.audio_queue.empty():
                peek_event = self.audio_queue.queue[0]
                if isinstance(peek_event, StopSequenceEvent):
                    self.audio_queue.get()
                    print("[AudioEngine] Sequence Stopped")
                    break
                
            if node.tipo == "TEMPO":
                try:
                    current_bpm = int(node.valor)
                    beat_duration = 60.0 / current_bpm
                    print(f"[AudioEngine] Changed BPM to {current_bpm}")
                except Exception: pass
                continue
                
            if node.tipo == "NOTA":
                pitch = self._get_pitch(node.valor)
                print(f"[AudioEngine] SequenceNote: {node.valor} -> {pitch} (Vol: {self.volume}, BPM: {current_bpm})")
                self.player.note_on(pitch, self.volume)
                
                # Sleep based on BPM rather than static duration
                sleep(beat_duration)
                
                self.player.note_off(pitch, self.volume)
            elif node.tipo == "PAUSA":
                try:
                    pause_beats = float(node.valor)
                    print(f"[AudioEngine] Pause for {pause_beats} beats")
                    sleep(pause_beats * beat_duration)
                except Exception: pass
            elif node.tipo == "ACORDE":
                pass

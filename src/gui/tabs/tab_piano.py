import customtkinter as ctk
from src.gui.components.piano_key import PianoKey
from src.core.config import KEYBOARD_MAPPING
from src.core.events import PlayNoteEvent, StopNoteEvent

class TabPiano(ctk.CTkFrame):
    def __init__(self, master, audio_queue, is_recording_cb, append_text_cb, **kwargs):
        super().__init__(master, **kwargs)
        self.audio_queue = audio_queue
        self.is_recording_cb = is_recording_cb
        self.append_text_cb = append_text_cb
        self.current_octave = 4
        
        self.keys = {}
        
        # Dimensions
        w_width = 60
        w_height = 140
        b_width = 40
        b_height = 90
        
        white_keys = [('C4', 'D'), ('D4', 'F'), ('E4', 'G'), ('F4', 'H'), ('G4', 'J'), ('A4', 'K'), ('B4', 'L')]
        black_keys = [('C#4', 'R'), ('D#4', 'T'), ('F#4', 'Y'), ('G#4', 'U'), ('A#4', 'I')]
        
        # Container for keys to allow absolute positioning (Fixed width to center)
        self.container = ctk.CTkFrame(self, width=432, height=160, fg_color="transparent")
        self.container.pack(pady=10)
        
        # Draw white keys first
        x_offset = 0
        for note, bind in white_keys:
            key = PianoKey(self.container, note=note, bind_key=bind, on_click=self.play_note, on_release=self.stop_note, is_black=False, width=w_width, height=w_height)
            key.place(x=x_offset, y=0)
            self.keys[bind.lower()] = key
            x_offset += w_width + 2
            
        # Draw black keys on top
        b_positions = [
            w_width - b_width//2 + 1,                   # C#
            2*w_width - b_width//2 + 3,                 # D#
            4*w_width - b_width//2 + 7,                 # F#
            5*w_width - b_width//2 + 9,                 # G#
            6*w_width - b_width//2 + 11                 # A#
        ]
        
        for (note, bind), x_pos in zip(black_keys, b_positions):
            key = PianoKey(self.container, note=note, bind_key=bind, on_click=self.play_note, on_release=self.stop_note, is_black=True, width=b_width, height=b_height)
            key.place(x=x_pos, y=0)
            self.keys[bind.lower()] = key
            
        # We will schedule the binding to ensure toplevel is ready
        self.after(100, lambda: self.winfo_toplevel().bind("<KeyPress>", self._on_key_press))
        self.after(100, lambda: self.winfo_toplevel().bind("<KeyRelease>", self._on_key_release))

    def set_octave(self, octave: int):
        self.current_octave = octave
        import re
        for key in self.keys.values():
            base_no_digit = re.sub(r'\d+', '', key.note)
            key.note = f"{base_no_digit}{octave}"

    def play_note(self, note: str):
        self.audio_queue.put(PlayNoteEvent(nota=note))
        if self.is_recording_cb():
            self.append_text_cb(note)

    def stop_note(self, note: str):
        self.audio_queue.put(StopNoteEvent(nota=note))

    def _on_key_press(self, event):
        key = event.char.lower()
        
        # Check if the focus is on the textbox
        focused_widget = self.focus_get()
        if focused_widget is not None and "textbox" in str(focused_widget).lower():
            return
            
        if key in self.keys:
            if getattr(self, f"_pressed_{key}", False):
                return
            setattr(self, f"_pressed_{key}", True)
            
            self.keys[key].set_active(True)
            self.play_note(self.keys[key].note)

    def _on_key_release(self, event):
        key = event.char.lower()
        if key in self.keys:
            setattr(self, f"_pressed_{key}", False)
            self.keys[key].set_active(False)
            self.stop_note(self.keys[key].note)
            if self.is_recording_cb():
                self.append_text_cb(self.keys[key].note + " ")

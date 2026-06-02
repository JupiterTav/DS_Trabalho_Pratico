import os
import tkinter.filedialog as filedialog

class IOManager:
    @staticmethod
    def load_text():
        filepath = filedialog.askopenfilename(
            title="Open DSL File",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filepath:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read(), filepath
        return None, None

    @staticmethod
    def save_text(text: str):
        filepath = filedialog.asksaveasfilename(
            title="Save DSL File",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filepath:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(text)
            return filepath
        return None

    @staticmethod
    def get_midi_save_path():
        filepath = filedialog.asksaveasfilename(
            title="Export MIDI",
            defaultextension=".mid",
            filetypes=[("MIDI Files", "*.mid"), ("All Files", "*.*")]
        )
        return filepath

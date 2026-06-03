import tkinter.filedialog as filedialog
import pathlib

class IOManager:
    @staticmethod
    def carrega_texto():
        filepath = filedialog.askopenfilename(
            title="Abrir arquivo texto",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filepath:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read(), filepath
        return None, None

    @staticmethod
    def get_output_path() -> pathlib.Path:
        filepath = filedialog.asksaveasfilename(
            title="Salvar saída",
            defaultextension=".wav",
            filetypes=[("wav", "*.wav"), ("mp3", "*.mp3"), ("ogg", "*.ogg")])
    
        return pathlib.Path(filepath)
